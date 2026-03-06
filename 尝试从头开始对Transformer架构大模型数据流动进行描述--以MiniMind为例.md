![LLM-structure.png](https://github.com/jingyaogong/minimind/blob/master/images/LLM-structure.png?raw=true)

# Pretrain与预测

dataloader加载数据集，使用Tokenizer把数据的输入转化为一个个的token_id，为了方便并行计算，后同步添加<PAD>这个toekn来实现整体数据输入长度的对齐（对齐seq_len）

- 这里其实有一个小知识点，就是pad是对序列进行左填充还是右填充

  在训练的时候如果必须要填充，往往是右填充，因为mask机制的存在可以是的模型不关注最右侧的PAD token。在真实训练的时候，其实不会添加什么padding，因为为了最高效，会直接把数据全部拼接在一起，依据max token len进行切分，反正有EOS这个特殊token的存在，模型会学到东西的；
  在推理的时候更多选用的都是左填充，因为左填充可以实现输入数据的last token还是有意义的token（不考虑<EOS>），从而在有意义的token影响下继续预测next token

接着把token_id序列输入**Embedding Layer**，取出每一个token对应的emb，拼接在一起的到一个原始的输入，假设batch_size为2，seq_len为8，hidden_size为512，那么得到的就是一个[2,8,512]的张量，这样的张量数据输入Transformer块组中。

在每一个Transformer块中，输入内容经过这样的运算：

1. 首先输入张量[2,8,512]要保留一份拷贝，方便后续的残差链接，然后经过归一化层，比如RMSNorm，把每一个样本的特征维度进行归一
   [2,8,512] -> RMSNorm -> [2,8,512] （方差被归一）
2. 接着是归一化的结果分别和三个矩阵相乘，得到Q，K，V矩阵，考虑到这里用的是GQA，假设有8个attention头，每两个头公用K和V，所以总共4组KV头，每一组需要复制一份，那么各种张量形状如下：
   1. Q：[2,8,512] -> W_q(x) -> [2,8,512] --特征维度拆分--> [2,8,8,64] （GQA不急着view换列）
   2. K : [2,8,512] -> W_k(x) -> [2,8,256] --特征维度拆分--> [2,8,4,64]
   3. V : [2,8,512] -> W_v(x) -> [2,8,256] --特征维度拆分--> [2,8,4,64]
   4. 对Q和K应用位置编码
   5. K和V拼接旧KV Cache中的内容
   6. K和V每组复制一份，自己拼接自己，构成 [2,8,8,64] 和Q一样的样式
   7. 对QKV进行view操作，分别transpose(1,2)为[2,8,8,64]
   8. 计算score：softmax括起来的那个；如果有mask，就应用mask
   9. sofrmax得到attn，attn进行dropout，之后和V进行矩阵乘法
   10. 交换1，2维度，重新view回B，L，D[2,8,512]
   11. 过一个线性层，再dropout
   12. 残差链接
3. 注意力计算后，进入FFN层，仍旧先保留一份用来残差链接，然后过归一化
4. 升维操作，使用SwiGLU激活函数，做法：
   1. 常规Transformer是把D升维为4D后激活再降维，总参数量为d\*4d\*2 =8 d² 
   2. $SwiGLU = SiLU(WX+b) \otimes (VX+c) , FFN(x) = (Swish(xW) \otimes xV)W2$，对于FFN层总共有W，V，W2三个权重，为了保证最后的总参数量一致，让每一个权重的维度变为$\frac{8}{3}D$。
   3. 线性变换之后dropout，再残差链接，得到输出
5. 块内运行的结果还是[2,8,512]，然后过RMSNorm进行归一
6. 归一之后进行线性运算：$xW,$ W的in_features为512，out_features为vocab size，实现对整个词表的logits映射
7. 采样始终只关注最后一个token都logits，因此只取logits[:, -1, :]，得到形状[2,vocab_size]
8. 映射后在最后一个维度softmax，得到每一个词的输出概率。这里牵扯到的知识点：
   temperature温度超参数、top-k采样、top-p采样（核采样）、beam search
   综合起来的流程为：
   1. logits除以温度超参数，来改变logits的分布情况，大于1的温度使得模型softmax之后概率分布更加平缓；小于1的温度使得softmax结果更加尖锐；设置为0往往代表着贪婪解码，只选用概率最高的token
   2. logits经过温度变化后，进行topk采样，logits里面只有前k个最大的logits保留原始结果，其他的都置为-inf，使得softmax之后他们的概率为0
   3. 接下来过softmax函数，现在只有k个token有对应的概率
   4. 把概率排序，从最大的概率开始累加概率和，如果概率和大于等于了定义好的p，那么就停止，将剩余的token概率都置为-inf
   5. 再次使用softmax求概率，然后再进行采样
   6. beam search则保留多个采样路径，采样路径的惩罚后概率是最高的。
9. 采样得到下一个token 的token_id，再去decode一下，映射回单词，拼接到序列后面，就完成了一次预测。
10. 对于pretrain，采用的策略是teacher forcing，每一次都选用真实的下一个token，而不是预测出来的采样的token，用这个来计算交叉熵，反向传播，更新参数。
"""
MinHash 与 SimHash 的纯 Python 实现。

这个文件的目标不是追求工业级极致性能，而是提供一个：
1. 便于学习和阅读的参考实现
2. 不依赖第三方库，开箱即可运行
3. 注释尽量详细，方便理解两种算法的核心思想

适用场景：
- MinHash：近似估计两个集合的 Jaccard 相似度
- SimHash：近似检测文本或特征向量的“指纹相似性”
"""

from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple


def _stable_hash(text: str, hash_bits: int = 64) -> int:
    """
    计算稳定的整数哈希值。

    为什么不直接用 Python 内置的 hash()？
    - Python 的 hash() 在不同进程中默认带随机种子
    - 这意味着同一段文本在不同次运行时，结果可能不同
    - 对于 MinHash / SimHash 这类需要“可复现指纹”的算法，不合适

    这里使用 hashlib 的 SHA-256：
    - 输出稳定
    - 所有平台一致
    - 然后截取前若干 bit 作为我们需要的整数哈希值

    参数：
    - text: 待哈希的字符串
    - hash_bits: 输出哈希位数，常见取值是 32 / 64 / 128

    返回：
    - 一个非负整数，表示 text 的稳定哈希结果
    """
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    digest_int = int.from_bytes(digest, byteorder="big", signed=False)
    mask = (1 << hash_bits) - 1
    return digest_int & mask


def tokenize(text: str) -> List[str]:
    """
    对文本做一个非常基础的分词/切词。

    这里采用的是“教学友好”的最简方案：
    - 英文统一转小写
    - 提取连续的字母数字下划线
    - 对中文场景，这种方式不会做真正中文分词

    如果你要在中文业务里更准确地使用：
    - 可以替换成按字切分
    - 也可以接入 jieba、pkuseg 等中文分词器
    - 或者直接把外部已提取好的特征传给 MinHash / SimHash

    例如：
    "Machine Learning, learning!" -> ["machine", "learning", "learning"]
    """
    return re.findall(r"\w+", text.lower())


@dataclass
class MinHash:
    """
    MinHash 近似算法。

    核心思想：
    - 对一个集合中的每个元素做若干组不同的哈希变换
    - 对每组变换，保留“最小哈希值”
    - 得到的最小值序列就是该集合的签名（signature）
    - 两个集合签名中相同位置的比例，可以近似它们的 Jaccard 相似度

    为什么它能近似 Jaccard？
    - 对于一个随机排列（或足够像随机排列的哈希函数），
      两个集合在该排列下的最小元素相同的概率，恰好等于它们的 Jaccard 相似度
    - 多次独立重复后，统计相同最小值的比例，就能得到近似估计

    参数：
    - num_hashes: 使用多少组哈希函数。越大越准，但计算和存储成本也越高
    - hash_bits: 单个哈希值保留多少位
    - seed: 用来生成哈希函数参数的种子，仅用于保证可复现
    """

    num_hashes: int = 128
    hash_bits: int = 64
    seed: int = 42

    def __post_init__(self) -> None:
        if self.num_hashes <= 0:
            raise ValueError("num_hashes 必须大于 0")
        if self.hash_bits <= 0 or self.hash_bits > 256:
            raise ValueError("hash_bits 必须在 1 到 256 之间")

        # 为了模拟多组不同的哈希函数，我们采用如下形式：
        # h_i(x) = (a_i * x + b_i) mod P
        #
        # 这里：
        # - x 是元素的基础整数哈希
        # - a_i / b_i 是每一组哈希函数对应的参数
        # - P 取一个足够大的质数
        #
        # 这不是唯一实现方式，但非常常见且便于理解。
        self._prime = (1 << 61) - 1
        self._max_hash = (1 << self.hash_bits) - 1
        self._hash_params = self._build_hash_params()

    def _build_hash_params(self) -> List[Tuple[int, int]]:
        """
        构造 num_hashes 组哈希函数参数。

        这里不使用 random 模块，目的是避免依赖运行时全局状态。
        我们用稳定哈希来派生参数，这样同样的 seed 一定生成同样的参数。
        """
        params: List[Tuple[int, int]] = []
        for i in range(self.num_hashes):
            # a 不能为 0，否则会退化成常数函数
            a = _stable_hash(f"minhash-a-{self.seed}-{i}", self.hash_bits) % self._prime
            if a == 0:
                a = i + 1

            b = _stable_hash(f"minhash-b-{self.seed}-{i}", self.hash_bits) % self._prime
            params.append((a, b))
        return params

    def signature(self, tokens: Iterable[str]) -> List[int]:
        """
        为一个 token 集合生成 MinHash 签名。

        注意：
        - MinHash 处理的是“集合相似度”
        - 因此同一个 token 出现多次并不会额外提高权重
        - 我们会先转成 set，自动去重

        返回：
        - 长度为 num_hashes 的整数列表
        """
        unique_tokens = set(tokens)
        if not unique_tokens:
            raise ValueError("tokens 不能为空；空集合无法生成有效的 MinHash 签名")

        # 初始化为“无限大”，后续不断取更小值
        signature = [math.inf] * self.num_hashes

        for token in unique_tokens:
            base_hash = _stable_hash(token, self.hash_bits)

            for idx, (a, b) in enumerate(self._hash_params):
                transformed = (a * base_hash + b) % self._prime
                transformed &= self._max_hash

                if transformed < signature[idx]:
                    signature[idx] = transformed

        return [int(value) for value in signature]

    def similarity(self, tokens_a: Iterable[str], tokens_b: Iterable[str]) -> float:
        """
        使用 MinHash 签名近似估计两个 token 集合的 Jaccard 相似度。

        估计方法：
        - 分别求出两个集合的 signature
        - 统计相同位置上哈希值相等的次数
        - 次数 / num_hashes 即近似相似度
        """
        sig_a = self.signature(tokens_a)
        sig_b = self.signature(tokens_b)
        same_count = sum(1 for left, right in zip(sig_a, sig_b) if left == right)
        return same_count / self.num_hashes

    @staticmethod
    def jaccard_similarity(tokens_a: Iterable[str], tokens_b: Iterable[str]) -> float:
        """
        计算真实的 Jaccard 相似度，方便和 MinHash 估计值做对比。

        Jaccard(A, B) = |A ∩ B| / |A ∪ B|
        """
        set_a = set(tokens_a)
        set_b = set(tokens_b)
        union = set_a | set_b
        if not union:
            return 1.0
        return len(set_a & set_b) / len(union)


@dataclass
class SimHash:
    """
    SimHash 指纹算法。

    SimHash 的目标：
    - 把一段文本或一个特征集合压缩成一个固定长度的二进制指纹
    - 相似文本的指纹通常只有少量 bit 不同
    - 因此可以通过海明距离（Hamming Distance）快速判断近似相似

    核心过程：
    1. 为每个特征计算一个固定长度的哈希值
    2. 对哈希值的每一位：
       - 如果这一位是 1，就给该维度加上特征权重
       - 如果这一位是 0，就给该维度减去特征权重
    3. 所有特征累计结束后：
       - 某一位总和 > 0，则最终指纹该位为 1
       - 否则该位为 0

    直观理解：
    - 每个特征都在“投票”
    - 相似文本通常共享大量相似特征，因此最终 bit 结果也更接近

    参数：
    - hash_bits: 生成多少位的 SimHash 指纹，常见值为 64
    """

    hash_bits: int = 64

    def __post_init__(self) -> None:
        if self.hash_bits <= 0 or self.hash_bits > 256:
            raise ValueError("hash_bits 必须在 1 到 256 之间")

    def fingerprint(self, weighted_tokens: Dict[str, float]) -> int:
        """
        根据“特征 -> 权重”字典生成 SimHash 指纹。

        参数：
        - weighted_tokens: 例如 {"apple": 2.0, "banana": 1.0}

        说明：
        - 权重可以是词频 TF，也可以是 TF-IDF，或者人为定义的重要性分数
        - 如果只想简单使用词频，直接把词出现次数作为权重即可
        """
        if not weighted_tokens:
            raise ValueError("weighted_tokens 不能为空")

        # vector 的每一维对应最终指纹的一位。
        # 它先累积“正负投票值”，最后再按正负号决定该位是 1 还是 0。
        vector = [0.0] * self.hash_bits

        for token, weight in weighted_tokens.items():
            if weight == 0:
                continue

            token_hash = _stable_hash(token, self.hash_bits)

            for bit_index in range(self.hash_bits):
                bit_mask = 1 << bit_index

                # 当前 bit 为 1 时加权重，为 0 时减权重
                if token_hash & bit_mask:
                    vector[bit_index] += weight
                else:
                    vector[bit_index] -= weight

        # 根据每一维的正负，生成最终二进制指纹
        fingerprint = 0
        for bit_index, value in enumerate(vector):
            if value > 0:
                fingerprint |= 1 << bit_index

        return fingerprint

    def from_tokens(self, tokens: Iterable[str]) -> int:
        """
        直接根据 token 序列生成 SimHash 指纹。

        这里采用最常见的简化方案：
        - 统计每个 token 的出现频次
        - 把词频作为权重输入 fingerprint()

        注意：
        - 与 MinHash 不同，SimHash 通常会考虑“重复出现”的影响
        - 所以这里不会去重，而是保留词频信息
        """
        weights: Dict[str, float] = {}
        for token in tokens:
            weights[token] = weights.get(token, 0.0) + 1.0
        return self.fingerprint(weights)

    @staticmethod
    def hamming_distance(left: int, right: int) -> int:
        """
        计算两个整数指纹的海明距离。

        海明距离定义：
        - 两个等长二进制串在多少个位上不同

        在 SimHash 中：
        - 海明距离越小，通常表示文本越相似
        """
        xor_value = left ^ right
        return xor_value.bit_count()

    def similarity(self, left: int, right: int) -> float:
        """
        把海明距离映射成一个 0 到 1 之间的“相似度分数”。

        这个分数不是像 Jaccard 那样有非常明确的集合论意义，
        只是为了更直观地展示距离大小：

        similarity = 1 - hamming_distance / hash_bits
        """
        distance = self.hamming_distance(left, right)
        return 1.0 - distance / self.hash_bits


def demo() -> None:
    """
    演示 MinHash 与 SimHash 的基本用法。

    运行方式：
    python minhash_simhash.py
    """
    text_a = "Machine learning makes it easier to build useful systems."
    text_b = "Machine learning helps us build practical and useful systems."

    tokens_a = tokenize(text_a)
    tokens_b = tokenize(text_b)

    print("文本 A tokens:", tokens_a)
    print("文本 B tokens:", tokens_b)
    print()

    # 1. MinHash 适合近似集合相似度（Jaccard）
    minhash = MinHash(num_hashes=128, hash_bits=64, seed=42)
    estimated = minhash.similarity(tokens_a, tokens_b)
    actual = MinHash.jaccard_similarity(tokens_a, tokens_b)

    print("=== MinHash ===")
    print(f"真实 Jaccard 相似度: {actual:.4f}")
    print(f"MinHash 估计相似度: {estimated:.4f}")
    print()

    # 2. SimHash 适合近似去重/近似文本匹配
    simhash = SimHash(hash_bits=64)
    fp_a = simhash.from_tokens(tokens_a)
    fp_b = simhash.from_tokens(tokens_b)
    distance = SimHash.hamming_distance(fp_a, fp_b)
    similarity = simhash.similarity(fp_a, fp_b)

    print("=== SimHash ===")
    print(f"指纹 A: {fp_a:016x}")
    print(f"指纹 B: {fp_b:016x}")
    print(f"海明距离: {distance}")
    print(f"归一化相似度: {similarity:.4f}")


if __name__ == "__main__":
    demo()

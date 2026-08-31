# 交叉熵
import numpy as np

def numpy_cross_entropy(logits, target):
    exps = np.exp(logits - np.max(logits, axis=1, keepdims=True))
    softmax_probs = exps / np.sum(exps, axis=1, keepdims=True)

    n = logits.shape[0]
    correct_logprobs = -np.log(softmax_probs[range(n), target] + 1e-12)
    loss = np.sum(correct_logprobs) / n
    return loss

import torch
import torch.nn as nn
import math

class LayerNorm(nn.Module):
    def __init__(self, normalized_shape, eps=1e-5, elementwise_affine=True):
        super().__init__()
        if isinstance(normalized_shape, int):
            normalized_shape = (normalized_shape, )
        self.normalized_shape = normalized_shape
        self.eps = eps
        self.elementwise_affine = elementwise_affine
        if elementwise_affine:
            self.gamma = nn.Parameter(torch.ones(self. normalized_shape))
            self.beta = nn.Parameter(torch.zeros(self.normalized_shape))
        else:
            self.gamma = None
            self.beta = None
    def forward(self, x):
        assert x.dim() >= len(self.normalized_shape)
        dims = list(range(-len(self.normalized_shape), 0))
        mean = x.mead(dim=dims, keepdim=True)
        var = x.var(dim=dims, keepdim=True, unbiased=False)
        std = math.sqrt(var + self.eps)
        x_normalized = (x-mean) / std
        if self.elementwise_affine:
            return self.gamma * x_normalized + self.beta
        return x_normalized

class RMSNorm(nn.Module):
    def __init__(self, normalized_shape, eps=1e-5, elementwise_affine=True):
        super().__init__()
        if isinstance(normalized_shape, int):
            normalized_shape = (normalized_shape, )
        self.normalized_shape = normalized_shape
        self.eps = eps
        self.elementwise_affine = elementwise_affine
        if self.elementwise_affine:
            self.gamma = nn.Parameter(torch.ones(self.normalized_shape))
        else:
            self.gamma = None
    def forward(self, x):
        assert x.dim() >= len(self.normalized_shape)
        dims = list(range(-len(self.normalized_shape), 0))
        RMS = x * torch.rsqrt(x.pow(2).mead(dim=dims, keepdim=True) + self.eps)
        if self.elementwise_affine:
            return self.gamma * RMS
        return RMS

class MultiHeadAttentionWithKVCache(nn.Module):
    def __init__(self, d_models, n_heads=8, dropout=0.1, bias=True):
        super().__init__()
        assert d_models % n_heads == 0
        self.d_k = d_models // n_heads
        self.n_heads = n_heads
        self.W_q = nn.Linear(d_models, d_models, bias)
        self.W_k = nn.Linear(d_models, d_models, bias)
        self.W_v = nn.Linear(d_models, d_models, bias)
        self.W_o = nn.Linear(d_models, d_models, bias)
        self.dropout = nn.Dropout(dropout)
    def forward(self, x, mask=None, past_key_value=None, use_cache=False):
        B,L,D = x.shape
        Q = self.W_q(x).view(B,L,self.n_heads, self.d_k).transpose(1,2)
        K = self.W_k(x).view(B,L,self.n_heads, self.d_k).transpose(1,2)
        V = self.W_v(x).view(B,L,self.n_heads, self.d_k).transpose(1,2)
        if past_key_value is not None:
            past_K, past_V = past_key_value
            K = torch.cat([past_K, K], dim=2)
            V = torch.cat([past_V, V], dim=2)
        present_key_value = (K,V) if use_cache else None

        score = torch.matmul(Q,K.transpose(-1,-2))/math.sqrt(self.d_k)
        if mask is not None:
            score = score.masked_fill(mask, float('-inf'))
        attn = torch.nn.functional.softmax(score, dim=-1)
        attn = self.dropout(attn)

        attn = torch.matmul(attn, V).transpose(1,2).contiguous().view(B,L,D)
        output = self.W_o(attn)
        return output, present_key_value

class GQA(nn.Module):
    def __init__(self, d_models, n_heads=8, repeat_times=2, dropout=0.1, bias=False):
        super().__init__()
        self.block_head = d_models // n_heads
        self.n_heads = n_heads
        self.repeat_times = repeat_times
        self.W_q = nn.Linear(d_models, self.block_head * self.n_heads, bias)
        self.W_k = nn.Linear(d_models, self.block_head * (self.n_heads // self.repeat_times), bias)
        self.W_v = nn.Linear(d_models, self.block_head * (self.n_heads // self.repeat_times), bias)
        self.W_o = nn.Linear(d_models, self.block_head * self.n_heads, bias)

        self.dropout = nn.Dropout(dropout)
    def _repeat_kv_block(self, K, V):
        return (torch.cat([K,K],dim=-1), torch.cat([V,V], dim=-1))

    def forward(self, x, mask:None, past_key_value=None, use_cache=False):
        B,L,D = x.shape
        Q = self.W_q(x).view(B,L,self.n_heads, self.block_head)
        K = self.W_k(x).view(B,L,self.n_heads//self.repeat_times, self.block_head)
        V = self.W_v(x).view(B,L,self.n_heads//self.repeat_times, self.block_head)

        if past_key_value is not None:
            past_k, past_v = past_key_value
            K, V = torch.cat([past_k, K], dim=1), torch.cat([past_v, V], dim=1)
        present_key_value = (K,V) if use_cache else None

        K, V = self._repeat_kv_block(K, V)

        Q = Q.transpose(1,2)
        K = K.transpose(1,2)
        V = V.transpose(1,2)

        score = torch.matmul(Q,K.transpose(-1,-2)) / math.sqrt(self.block_head * self.n_heads)
        if mask is not None:
            score = score.masked_fill(mask, float('-inf'))
        attn = torch.nn.funcitonal.softmax(score)
        attn = self.dropout(attn)

        attn = torch.matmul(attn, V).transpose(-1, -2).contiguous().view(B,L,D)
        output = self.W_o(attn)
        return output, present_key_value
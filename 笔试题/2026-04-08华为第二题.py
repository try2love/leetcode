# 目标：返回权重值

import sys
import math
# If you need to import additional packages or classes, please import here.

def cal_loss(y_pred, y_true):
    return sum((y_pred[i]-y_true[i])**2 for i in range(len(y_pred)))/(2*len(y_pred))

def normalize(x): # 输入x1, x2, x3，得到归一化的结果
    tmp_max, tmp_min= max(x), min(x)
    if tmp_max == tmp_min:
        return [0]*len(x), tmp_max, tmp_min
    return [(x[i]-tmp_min)/(tmp_max-tmp_min) for i in range(len(x))], tmp_max, tmp_min

def update(w0, w1, w2, w3, y_pred, y_true, x1, x2, x3, alpha):
    # tmp = sum([y_pred[i]-y_true[i] for i in range(len(y_pred))])
    m = len(y_pred)
    w0 = w0 - alpha*sum([y_pred[i]-y_true[i] for i in range(len(y_pred))])/m
    w1 = w1 - alpha*sum([(y_pred[i]-y_true[i])*x1[i] for i in range(len(y_pred))])/m
    w2 = w2 - alpha*sum([(y_pred[i]-y_true[i])*x2[i] for i in range(len(y_pred))])/m
    w3 = w3 - alpha*sum([(y_pred[i]-y_true[i])*x3[i] for i in range(len(y_pred))])/m
    return w0, w1, w2, w3

def forward(m, w0, w1, w2, w3, x1, x2, x3):
    # 依赖当前的权重计算y_pred
    y_pred = []
    for i in range(m):
        y_pred.append(w0 + w1*x1[i] + w2*x2[i] + w3*x3[i])
    return y_pred

def de_normalize(w, tmp_max, tmp_min):
    if tmp_max==tmp_min:
        return 0
    return w/(tmp_max-tmp_min)

def refine_w0(w0, w1, w2, w3, x1_min, x2_min, x3_min):
    return w0 - sum(w1*x1_min, w2*x2_min, w3*x3_min)
    
def diedai(N, m, w0, w1, w2, w3, x1, x2, x3, y, alpha,x1_max, x1_min,x2_max, x2_min,x3_max, x3_min):
    # 迭代
    for _ in range(N):
        y_pred = forward(m, w0, w1, w2, w3, x1, x2, x3)
        loss = cal_loss(y_pred, y)
        w0, w1, w2, w3 = update(w0, w1, w2, w3, y_pred, y, x1, x2, x3, alpha)
    w1 = de_normalize(w1, x1_max, x1_min)
    w2 = de_normalize(w2, x2_max, x2_min)
    w3 = de_normalize(w3, x3_max, x3_min)
    w0 = refine_w0(w0, w1, w2, w3, x1_min, x2_min, x3_min)
    return w0, w1, w2, w3

def func():
    m = eval(input())
    N = eval(input())
    alpha = eval(input())
    x1, x2, x3, y = [0]*m, [0]*m, [0]*m, [0]*m
    for i in range(m):
        nums = list(map(int, sys.stdin.readline().strip().split()))
        x1[i], x2[i], x3[i], y[i] = nums
        
    # 数据收集完毕
    x1, x1_max, x1_min = normalize(x1)
    x2, x2_max, x2_min = normalize(x2)
    x3, x3_max, x3_min = normalize(x3)
    w0, w1, w2, w3 = diedai(N, m, w0, w1, w2, w3, x1, x2, x3, y, alpha,x1_max, x1_min,x2_max, x2_min,x3_max, x3_min)
    print(w0,end=" ")
    print(w1,end=" ")
    print(w2,end=" ")
    print(w3,end=" ")

if __name__ == "__main__":
    func()

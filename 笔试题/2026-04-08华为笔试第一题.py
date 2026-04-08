# 核心目标：KMeans算法聚类，然后算花费时间
import sys
import math
from typing import List
from collections import Counter

max_iters = 50 # 最大迭代次数
tol = 1e-4 # 移动距离之和的最小值

def calculate_dis(x:float=0.0, y:float=0.0, center_x:float=0.0, center_y:float=0.0):
    # 计算(x,y)和中心点之间的距离
    return math.sqrt((center_x-x)**2 + (center_y-y)**2)

def k_means(pos:List[List[float]], centers:List[List[float]], K:int, times:int):
    if times >= max_iters:
        return centers
    # 实现Kmeans聚类，输入原始pos，输出迭代后的聚类中心
    dis = []
    cluster = [0] * len(pos)
    for i in range(len(pos)):
        x, y = pos[i]
        dis.append([calculate_dis(x,y,centers[j][0], centers[j][1]) for j in range(K)])
        min_dis = min(dis[i])
        cluster[i] = dis[i].index(min_dis)
    # 获取了当前的每一个元素对应类别标签
    cnt = Counter(cluster)
    # 所有标签一致的求和取平均
    sum_xy = [[0.0, 0.0]*K]
    for i in range(len(pos)):
        sum_xy[cluster[i]][0] += pos[i][0]
        sum_xy[cluster[i]][1] += pos[i][1]
    for i in range(K):
        sum_xy[i][0] /= cnt[i]
        sum_xy[i][1] /= cnt[i]
    # sum_xy就是最新的中心点
    if all([calculate_dis(sum_xy[i][0], sum_xy[i][1], centers[i][0], centers[i][1]) for i in range(K)][j]<tol for j in range(K)):
        return sum_xy
    return k_means(pos, sum_xy, K, times+1)

def cal_result(centers:List[List[float]], speed:int):
    # 假设输入为聚类中心的list，返回最后的时间
    # K个聚类中心，还要考虑路径的规划问题
    # 首先需要计算最小的路径长度，然后除以speed乘以3600即可
    pass

def solve():
    K, N, speed = list(map(int, sys.stdin.readline().strip().split()))
    pos = []
    for i in range(N):
        # N个包裹的位置
        pos.append(list(map(float, sys.stdin.readline().strip().split())))
    # 获取了所有的数据，先按照升序排序
    if K > N:
        init_dis = [calculate_dis(p[0],p[1]) for p in pos]
        indices = list(range(N)).sort(lambda dis: init_dis)
        # 需要获取所有中心坐标
        centers = [pos[indices[i]] for i in range(K)]
        centers = k_means(pos, centers, K, 0)   
    else:
        # 每一个都是中心坐标
        centers = pos
    print(cal_result(centers, speed))


if __name__ == "__main__":
    solve()

# --- Gemini给出的答案---
import sys
import math
from typing import List
from collections import Counter

max_iters = 50
tol = 1e-4

def calculate_dis(x1, y1, x2=0.0, y2=0.0):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def k_means(pos: List[List[float]], K: int):
    N = len(pos)
    if N <= K:
        return pos
    
    # 1. 初始化：取距离原点最近的 K 个点作为初始中心
    init_dis = [calculate_dis(p[0], p[1]) for p in pos]
    # 使用 sorted 获取索引
    indices = sorted(range(N), key=lambda i: init_dis[i])
    centers = [pos[indices[i]] for i in range(K)]

    for _ in range(max_iters):
        cluster = []
        # 2. 分配阶段
        for p in pos:
            distances = [calculate_dis(p[0], p[1], c[0], c[1]) for c in centers]
            cluster.append(distances.index(min(distances)))
        
        # 3. 更新阶段
        new_centers = [[0.0, 0.0] for _ in range(K)]
        counts = [0] * K
        for i in range(N):
            c_idx = cluster[i]
            new_centers[c_idx][0] += pos[i][0]
            new_centers[c_idx][1] += pos[i][1]
            counts[c_idx] += 1
        
        # 处理空聚类，防止除以 0
        for i in range(K):
            if counts[i] > 0:
                new_centers[i][0] /= counts[i]
                new_centers[i][1] /= counts[i]
            else:
                # 如果某个中心没点，随机指派一个点防止丢失中心
                new_centers[i] = pos[i % N]

        # 4. 收敛判断
        shift = sum(calculate_dis(new_centers[i][0], new_centers[i][1], centers[i][0], centers[i][1]) for i in range(K))
        centers = new_centers
        if shift < tol:
            break
            
    return centers

def cal_result(centers: List[List[float]], speed: int):
    if not centers: return 0.0
    # 路径规划：这里简单处理为回到原点的总距离（TSP问题的简化版）
    # 实际应用中可能需要更复杂的路径算法
    total_dis = 0.0
    curr_x, curr_y = 0.0, 0.0
    # 这里按顺序访问中心点并返回原点
    for c in centers:
        total_dis += calculate_dis(curr_x, curr_y, c[0], c[1])
        curr_x, curr_y = c[0], c[1]
    total_dis += calculate_dis(curr_x, curr_y, 0.0, 0.0) # 回到原点
    
    return (total_dis / speed) * 3600

def solve():
    line = sys.stdin.readline().strip()
    if not line: return
    K, N, speed = list(map(int, line.split()))
    pos = []
    for _ in range(N):
        pos.append(list(map(float, sys.stdin.readline().strip().split())))
    
    centers = k_means(pos, K)
    print(f"{cal_result(centers, speed):.2f}")

if __name__ == "__main__":
    solve()
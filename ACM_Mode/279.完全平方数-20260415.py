#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30403
#
# [279] 完全平方数
# 14:05 ACM AC，但是写起来感觉很别扭
import math
from math import inf
from functools import cache
from math import isqrt
# @lc code=start
# -----参考答案------
# 这是一个选或不选的问题，因此是动态规划
# 写在外面，多个测试数据可以共享，减少计算量
@cache
def dfs(i:int, j:int) -> int:
    if i == 0:
        return inf if j else 0
    if j < i * i:
        return dfs(i-1, j)
    return min(dfs(i-1,j), dfs(i, j-i*i)+1) # 不选和选

N = 10000
dp = [[0]*(N+1) for _ in range(isqrt(N)+1)]
dp[0] = [0] + [inf]*N
for i in range(1, len(dp)):
    for j in range(N+1):
        if j < i*i:
            dp[i][j] = dp[i-1][j] # 只能不选
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-i*i]+1) # 不选vs选

dp = [0] + [inf] * N
for i in range(1, isqrt(N)+1):
    for j in range(i*i, N+1):
        dp[j] = min(dp[j], dp[j-i*i]+1)
class Solution:
    def numSquares(self, n:int) -> int:
        return dfs(isqrt(n), n)
        return dp[isqrt(n)][n]
        return dp[n]

# -----参考答案------

# class Solution:
#     def numSquares(self, n: int) -> int:
#         nums = [x**2 for x in range(int(math.sqrt(n)), 0, -1)]
#         @cache
#         def dfs(i:int):
#             if i < 4:
#                 return i if i>=0 else inf
#             return min(dfs(i-x) for x in nums if x<=i)+1
#         return dfs(n)
        
# @lc code=end

n = eval(input())
sol = Solution()
print(sol.numSquares(n))

#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30404
#
# [279] 完全平方数
# 9:50 没写出来，6922这个case超时了
import math
from math import inf, isqrt
from functools import cache
# @lc code=start
@cache
def dfs(i:int, j:int) -> int:
    if i == 0:
        return inf if j else 0
    if j < i*i:
        return dfs(i-1, j)
    return min(dfs(i-1, j), dfs(i, j-i*i)+1)

N = 10000
f = [[0]*(N+1) for _ in range(isqrt(N)+1)]
f[0] = [0] + [inf]*N
for i in range(1, len(f)):
    for j in range(N+1):
        if j<i*i:
            f[i][j] = f[i-1][j]
        else:
            f[i][j] = min(f[i-1][j], f[i][j-i*i]+1)

class Solution:
    def numSquares(self, n: int) -> int:
        # 参考

        return f[isqrt(n)][n]

        return dfs(isqrt(n), n)


        # right = int(math.sqrt(n))
        # nums = [i**2 for i in range(right, 0, -1)]
        # print(nums)
        # @cache
        # def dfs(i:int, target):
        #     if target < 0 or i >= len(nums):
        #         return inf
        #     if target<=1:
        #         return target
        #     return min(dfs(i, target-nums[i]) + 1, dfs(i+1, target))
        # return dfs(0, n)
        
# @lc code=end

n= eval(input())
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


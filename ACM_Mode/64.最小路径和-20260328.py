#
# @lc app=leetcode.cn id=64 lang=python3
# @lcpr version=30401
#
# [64] 最小路径和
# 13:17 ACM AC 额外花费5:47转二维dp 额外花费1:22转为一维dp
from typing import List
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [inf] * (n+1)
        for i in range(m):
            dp[0] = inf
            for j in range(n):
                if i==j==0:
                    dp[j+1] = grid[0][0]
                else:
                    dp[j+1] = min(dp[j+1], dp[j]) + grid[i][j]
        return dp[-1]


        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0] = [inf] * (n+1)
        for i in range(m):
            dp[i+1][0] = inf
            for j in range(n):
                if i==j==0:
                    dp[i+1][j+1] = grid[0][0]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + grid[i][j]
        return dp[-1][-1]

        @cache
        def dfs(i:int, j:int):
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return grid[0][0]
            return min(dfs(i-1, j), dfs(i, j-1)) + grid[i][j]
        cost = dfs(m-1, n-1)
        return cost
# @lc code=end

import sys
lines = sys.stdin.readlines()
grid = []
for line in lines:
    grid.append(list(map(int, line.strip().split())))
sol = Solution()
print(sol.minPathSum(grid))

#
# @lcpr case=start
# [[1,3,1],[1,5,1],[4,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=64 lang=python3
# @lcpr version=30404
#
# [64] 最小路径和
# 4:56 ACM AC 8:21 DP AC 10:18 一维AC
from typing import List
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # ans = grid[-1][-1]
        m,n = len(grid), len(grid[0])
        dp = [inf] *(n+1)
        dp[1] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    continue
                dp[j+1] = min(dp[j+1], dp[j])+grid[i][j]
        return dp[-1]
        dp = [[inf]*(n+1) for _ in range(m+1)]
        dp[1][1] = grid[0][0]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + grid[i][j]
                dp[1][1] = grid[0][0]
        return dp[m][n]

        @cache
        def dfs(i:int, j:int):
            # 回溯问题
            if i<0 or i>=m or j<0 or j>=n:
                return inf
            if i==0 and j==0:
                return grid[i][j]
            return min(dfs(i-1, j), dfs(i,j-1))+grid[i][j]
        return dfs(m-1, n-1)
        
# @lc code=end



#
# @lcpr case=start
# [[1,3,1],[1,5,1],[4,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#


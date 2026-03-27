#
# @lc app=leetcode.cn id=62 lang=python3
# @lcpr version=30401
#
# [62] 不同路径
# 11:24 ACM AC，但是总感觉递归写的不熟练了
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # -----参考答案------
        dp = [0]*(n+1)
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    dp[1] = 1
                else:
                    dp[j+1] = dp[j+1] + dp[j]
        return dp[n]

        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    dp[1][1] = 1
                else:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        return dp[m][n]

        @cache
        def dfs(i:int, j:int):
            if i<0 or j<0:
                return 0
            if i==0 or j==0:
                return 1
            return dfs(i-1,j) + dfs(i,j-1)
        return dfs(m-1, n-1)
        # -----参考答案------

        # 感觉写不出来dp
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # dp[-1][-1] = 1
        # for i in range(m):
        #     for j in range(n):
        #         dp[i][j] = 

        ans = 0
        @cache
        def dfs(i:int, j:int):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            nonlocal ans
            return dfs(i,j+1) + dfs(i+1,j)
        ans = dfs(0,0)
        return ans
# @lc code=end

m = eval(input())
n = eval(input())
sol = Solution()
print(sol.uniquePaths(m,n))
#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=62 lang=python3
# @lcpr version=30404
#
# [62] 不同路径
# 3:00 ACM AC 13:18没写出来dp
from functools import cache
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cankao
        f = [[0]*(n+1) for _ in range(m+1)]
        f[0][1] = 1
        for i in range(m):
            for j in range(n):
                f[i+1][j+1] = f[i][j+1] + f[i+1][j]
        return f[m][n]

        f = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    f[1][1] = 1
                else:
                    f[i+1][j+1] = f[i][j+1] + f[i+1][j]
        return f[m][n]        
        @cache
        def dfs(i:int, j:int) -> int:
            if i<0 or j<0:
                return 0
            if i==0 and j==0:
                return 1
            return dfs(i-1,j) + dfs(i, j-1)
        return dfs(m-1, n-1)

        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if i==1 or j==1:
                    dp[i+1][j+1] = 1
                else:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j]
        print(dp)
        return dp[m][n]
        @cache
        def dfs(i:int, j:int):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            if i==0 or j==0:
                return 1
            return dfs(i-1,j) + dfs(i,j-1)
        # return dfs(0,0)
        return dfs(m-1, n-1)
# @lc code=end



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

#


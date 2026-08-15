#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30404
#
# [72] 编辑距离
# 2:03 ACM AC, 7:07 DP 8:21 DP 11:22一维错误
from functools import cache
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # cankao
        dp = [x for x in range(n+1)]
        for x in word1:
            pre = dp[0]
            dp[0] += 1
            for j, y in enumerate(word2):
                tmp = dp[j+1]
                dp[j+1] = pre if x==y else min(dp[j+1], dp[j], pre) + 1
                pre = tmp
        return dp[-1]

        dp = [x for x in range(n+1)]
        for i in range(m):
            for j in range(n-1, -1 ,-1):
                if word1[i] == word2[j]:
                    continue
                dp[j+1] = min(dp[j], dp[j+1])+1
        return dp[-1]

        dp = [[0]*(n+1) for _ in range(2)]
        dp[0] = [x for x in range(n+1)]
        for i in range(m):
            dp[(i+1)%2][0] = i+1
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[(i+1)%2][j+1] = dp[i%2][j]
                else:
                    dp[(i+1)%2][j+1] = min(dp[i%2][j], dp[i%2][j+1], dp[(i+1)%2][j]) + 1
        return dp[m%2][n]
    
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0] = [x for x in range(n+1)]
        for i in range(m):
            dp[i+1][0] = i+1
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1
        return dp[m][n]
        @cache
        def dfs(i:int ,j:int):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if word1[i] == word2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i-1,j-1), dfs(i-1, j), dfs(i, j-1))+1
        return dfs(m-1, n-1)
# @lc code=end



#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#


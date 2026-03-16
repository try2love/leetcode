#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30400
#
# [72] 编辑距离
# 5:07 核心的记忆化ac 8:19 ACM AC 16:50二维dp AC,初始化错误，所以看了答案
# 还是不太会这种二维转一维，应该存储哪一个临时变量
from functools import cache
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n+1))
        for i in range(m):
            pre = i
            dp[0] = i+1
            for j in range(n):
                tmp = dp[j+1]
                dp[j+1] = min(tmp+1, dp[j]+1, pre+(word1[i]!=word2[j]))
                pre = tmp
        return dp[n]
        # m, n = len(word1), len(word2)
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # dp[0] = list(range(n+1))
        # for i in range(m):
        #     dp[i+1][0] = i+1
        #     for j in range(n):
        #         dp[i+1][j+1] = min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j]+(word1[i]!=word2[j]))
        # return dp[m][n]
        # @cache
        # def dfs(i:int, j:int):
        #     if i<0 or j<0:
        #         return abs(i-j)
        #     return min(dfs(i-1,j)+1, dfs(i,j-1)+1, dfs(i-1,j-1)+(word1[i] != word2[j]))
        # return dfs(len(word1)-1, len(word2)-1)
# @lc code=end

import sys
word1 = input()
word2 = input()
sol = Solution()
print(sol.minDistance(word1, word2))

#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#


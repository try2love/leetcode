#
# @lc app=leetcode.cn id=1143 lang=python3
# @lcpr version=30400
#
# [1143] 最长公共子序列
# 4:08 ACM AC 6:12 二维dp 8:56 一维dp
from functools import cache
# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] *(n+1)
        for i,x in enumerate(text1):
            pre = 0
            for j,y in enumerate(text2):
                tmp = dp[j+1]
                if x==y:
                    dp[j+1] = pre + 1
                else:
                    dp[j+1] = max(dp[j], tmp)
                pre = tmp
        return dp[n]

        # dp = [[0] *(n+1) for _ in range(m+1)]
        # for i,x in enumerate(text1):
        #     for j,y in enumerate(text2):
        #         if x==y:
        #             dp[i+1][j+1] = dp[i][j] + 1
        #         else:
        #             dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        # return dp[m][n]

        # @cache
        # def dfs(i:int, j:int):
        #     if i<0 or j<0:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return dfs(i-1,j-1) + 1
        #     return max(dfs(i,j-1), dfs(i-1,j))
        # return dfs(m-1, n-1)
# @lc code=end
import sys
text1 = sys.stdin.readline().strip()
text2 = sys.stdin.readline().strip()
sol = Solution()
print(sol.longestCommonSubsequence(text1, text2))


#
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#


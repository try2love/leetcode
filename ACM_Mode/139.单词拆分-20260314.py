#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30400
#
# [139] 单词拆分
# 目前只能想到用回溯
# 21:45提交，但是超时了，添加上记忆化搜索就正确了 ACM的输入输出正确。
from typing import List
from itertools import cache
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len, wordDict))
        words = set(wordDict)

        n = len(s)
        dp = [True] + [False]*n
        for i in range(1, n+1):
            for j in range(i-1, max(i-max_len-1, -1), -1):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]

        # 正确的记忆化搜索
        # @cache
        # def dfs(i:int):
        #     if i==0:
        #         return True
        #     for j in range(i-1, max(i-max_len-1,-1), -1):
        #         if s[j:i] in words and dfs(j):
        #             return True
        #     return False
        # return dfs(len(s))

        # if wordDict is None:
        #     return True if s is None else False
        # @ cache
        # def dfs(s):
        #     if s == "":
        #         return True
        #     flag = False
        #     for word in wordDict:
        #         i = len(word)
        #         if s[:i] in wordDict:
        #             flag = flag or dfs(s[i:])
        #     return flag
        # return dfs(s)
    
        # 下面是最早写的
        # 现在只能想起来回溯
        # wordDict = set(wordDict)
        # @ cache
        # def dfs(s):
        #     if s == "":
        #         return True
        #     flag = False
        #     for i in range(1, len(s)+1):
        #         if s[:i] in wordDict:
        #             flag = flag or dfs(s[i:])
        #     return flag
        # return dfs(s)
# @lc code=end

import sys
s = sys.stdin.readline().strip()
wordDict = sys.stdin.readline().strip().split()
sol = Solution()
print(sol.wordBreak(s, wordDict))

#
# @lcpr case=start
# "leetcode"\n["leet","code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple","pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#


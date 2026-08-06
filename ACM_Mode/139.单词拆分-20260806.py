#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30404
#
# [139] 单词拆分
# 9:45 ACM AC 15:30 DP错误
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 参考
        max_len = max(map(len, wordDict))
        words = set(wordDict)
        n = len(s)
        f = [True] + [False]*n
        for i in range(1, n+1):
            f[i] = any(f[j] and s[j:i] in words for j in range(i-1, max(i-max_len-1,-1),-1))
        return f[n]

        for i in range(1, n+1):
            for j in range(i-1, max(i-max_len-1, -1), -1):
                if f[j] and s[j:i] in words:
                    f[i] = True
                    break
        return f[n]
        
        max_len = max(map(len, wordDict))
        words = set(wordDict)
        @cache
        def dfs(i:int) -> bool:
            if i == 0:
                return True
            return any(s[j:i] in words and dfs(j) for j in range(i-1, max(i-max_len-1,-1),-1))
        return dfs(len(s))

        max_len = max(map(len, wordDict))
        words = set(wordDict)
        @cache
        def dfs(i:int)->bool:
            if i==0:
                return True
            for j in range(i-1, max(i-max_len-1, -1), -1):
                if s[j:i] in words and dfs(j):
                    return True
            return False
        return dfs(len(s))

        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)):
            for x in wordDict:
                if s[i:i+len(x)] == x:
                    dp[i] = dp[i+len(x)] or dp[i]
                else:
                    dp[i] = dp[i] or False
        return dp[0]
    
        @cache
        def dfs(i:int):
            if i >= len(s):
                return True
            inner = []
            for x in wordDict:
                if s[i:i+len(x)] == x:
                    inner.append(dfs(i+len(x)))
                else:
                    inner.append(False)
            return any(inner)

        return dfs(0)
        
# @lc code=end



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


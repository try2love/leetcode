#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30404
#
# [72] 编辑距离
# 9:23 没做出来
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 参考
        f = list(range(len(word2) + 1))
        for x in word1:
            pre = f[0]
            f[0] += 1  # f[0] = i + 1
            for j, y in enumerate(word2):
                tmp = f[j + 1]
                f[j + 1] = pre if x == y else min(f[j + 1], f[j], pre) + 1
                pre = tmp
        return f[-1]

        n, m = len(word1), len(word2)
        @cache
        def dfs(i:int, j:int) -> int:
            if i<0: return j+1
            if j<0: return i+1
            if word1[i] == word2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i-1, j), dfs(i, j-1), dfs(i-1, j-1)) + 1
        return dfs(n-1, m-1)


        @cache
        def dfs(i:int, j:int):
            if i<0:
                return j+1 if j>=0 else inf
            if j<0:
                return i+1 if i>=0 else inf
            if word1[i] == word2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i-1, j-1), dfs(i, j-1), dfs(i-1,j))+1
        return dfs(len(word1)-1, len(word2)-1)
        
# @lc code=end



#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#


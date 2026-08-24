#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30404
#
# [14] 最长公共前缀
# 6:39 aCM aC
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 参考
        s0 = strs[0]
        for j,c in enumerate(s0):
            for s in strs:
                if j==len(s) or s[j] != c:
                    return s0[:j]
        return s0

        if len(strs) == 1:
            return strs[0]
        i = 0
        while i < min([len(s) for s in strs]):
            cur = strs[0][i]
            j = 1
            while j < len(strs):
                if strs[j][i] != cur:
                    return strs[0][:i]
                else:
                    j += 1
            i += 1
        return strs[0][:i]
# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#


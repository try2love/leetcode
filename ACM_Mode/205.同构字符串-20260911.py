#
# @lc app=leetcode.cn id=205 lang=python3
# @lcpr version=30404
#
# [205] 同构字符串
# 12:52 ACM AC
from collections import defaultdict
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 参考答案
        s2t, t2s = {}, {}
        for a,b in zip(s,t):
            if a in s2t and s2t[a] != b or b in t2s and t2s[b] != a:
                return False
            s2t[a], t2s[b] = b, a
        return True

        # pos = [""] * 26
        # for i,ch in enumerate(t):
        #     if pos[ord(s[i])-ord('a')] == "":
        #         pos[ord(s[i])-ord('a')] = ch
        #     elif pos[ord(s[i])-ord('a')] != ch:
        #         return False
        #     # print(pos)
        # return True

        hash_map = {}
        hash_map_2 = {}
        for i,ch in enumerate(s):
            if ch not in hash_map:
                hash_map[ch] = t[i]
            elif hash_map[ch] != t[i]:
                return False
            if t[i] not in hash_map_2:
                hash_map_2[t[i]] = ch
            elif hash_map_2[t[i]] != ch:
                return False
        return True
        
# @lc code=end

s = "badc"
t = "baba"
sol = Solution()
print(sol.isIsomorphic(s,t))


#
# @lcpr case=start
# "egg"\n"add"\n
# @lcpr case=end

# @lcpr case=start
# "foo"\n"bar"\n
# @lcpr case=end

# @lcpr case=start
# "paper"\n"title"\n
# @lcpr case=end

#


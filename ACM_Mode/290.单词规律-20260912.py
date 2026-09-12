#
# @lc app=leetcode.cn id=290 lang=python3
# @lcpr version=30404
#
# [290] 单词规律
# 6:27 ACM AC

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 参考答案
        res = s.split()
        return list(map(pattern.index, pattern)) == list(map(res.index, res))

        s_p = s.split(' ')
        return len(pattern) == len(s_p) and len(set(zip(pattern, s_p))) == len(set(s_p)) == len(set(pattern))

        hash_map = {}
        hash_map2 = {}
        tmp = s.split()
        if len(pattern) != len(tmp):
            return False
        for i,ch in enumerate(pattern):
            if ch in hash_map and hash_map[ch] != tmp[i]:
                return False
            elif ch not in hash_map:
                hash_map[ch] = tmp[i]
            if tmp[i] in hash_map2 and hash_map2[tmp[i]] != ch:
                return False
            elif tmp[i] not in hash_map2:
                hash_map2[tmp[i]] = ch
        return True

# @lc code=end



#
# @lcpr case=start
# "abba"\n"dog cat cat dog"\n
# @lcpr case=end

# @lcpr case=start
# "abba"\n"dog cat cat fish"\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n"dog cat cat dog"\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30404
#
# [49] 字母异位词分组
# 9:44 ACm AC
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 参考答案
        d = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())

        d = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in d:
                d[sorted_s] = []
            d[sorted_s].append(s)
        return list(d.values())

        ans = []
        hash_map = {}
        for x in strs:
            tmp = "".join(sorted([y for y in x]))
            if tmp in hash_map:
                hash_map[tmp].append(x)
            else:
                hash_map[tmp] = [x]
        for key in hash_map:
            ans.append(hash_map[key])
        return ans
        
# @lc code=end



#
# @lcpr case=start
# ["eat","tea","tan","ate","nat","bat"]\n
# @lcpr case=end

# @lcpr case=start
# [""]\n
# @lcpr case=end

# @lcpr case=start
# ["a"]\n
# @lcpr case=end

#


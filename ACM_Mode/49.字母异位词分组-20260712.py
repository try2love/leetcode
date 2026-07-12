#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30404
#
# [49] 字母异位词分组
# 8:19 ACM AC
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
        
        hash_map = defaultdict(list)
        # tmp = [cur.sorted() for cur in strs]
        for idx, cur in enumerate(strs):
            hash_map[str(sorted(cur))].append(cur)
        ans = []
        for x in hash_map:
            ans.append(hash_map[x])
        return ans

# @lc code=end

import sys
import json
strs = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.groupAnagrams(strs))

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


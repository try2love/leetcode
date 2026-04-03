#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30402
#
# [49] 字母异位词分组
# 11:46 ACM AC
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # -----参考答案------
        # 优雅 真的是太优雅了
        d = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())
        # -----参考答案------

        # 这种题我知道是看每一个的cnt一致不一致，但是cnt不能作为键，怎么办？
        # 每一个都sorted，然后维护一个哈希表，list
        tmp = ["".join(sorted(x)) for x in strs]
        # print(tmp, type(tmp))
        cnt = defaultdict(list)
        for idx, x in enumerate(tmp):
            cnt[x].append(idx)
        ans = []
        # 如何遍历key和val？
        for val in cnt.values():
            ans.append([strs[i] for i in val])
        return ans

# @lc code=end
import sys
import json
strs = json.loads(sys.stdin.readline().strip())
print(strs, type(strs))
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


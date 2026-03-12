#
# @lc app=leetcode.cn id=49 lang=python3
# @lcpr version=30400
#
# [49] 字母异位词分组
#
import sys
from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            d[sorted_s].append(s)
        return list(d.values())
# @lc code=end

# 通过输入读取
# data = sys.stdin.read().strip().split()
# if data[0].isdigit():
#     n = int(data[0])
#     strs = data[1:1+n]
# else:
#     strs = data

# solution = Solution()
# result = solution.groupAnagrams(strs)
# for group in result:
#     print(" ".join(group))

# 构造测试用例列表
test_cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    ["abc", "bac", "cab"],
    ["a"],
    [""]
]

# 逐个测试
solution = Solution()
for i, case in enumerate(test_cases, 1):
    print(f"Test case {i}: {case}")
    result = solution.groupAnagrams(case)
    print(result)
    # for group in result:
    #     print(' '.join(group))
    print()

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


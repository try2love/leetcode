#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30402
#
# [1] 两数之和
# 4:00 ACM AC
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 一个循环
        hash_map = {}
        for idx, x in enumerate(nums):
            if target-x in hash_map:
                return [hash_map[target - x], idx]
            hash_map[x] = idx
        return []

        hash_map = defaultdict(int)
        for idx, x in enumerate(nums):
            hash_map[x] = idx
        for idx, x in enumerate(nums):
            if target - x in hash_map and hash_map[target - x]!=idx:
                return [idx, hash_map[target - x]]
        return []

# @lc code=end
import sys
import json
nums = json.loads(sys.stdin.readline().strip())
target = eval(input())
sol = Solution()
print(sol.twoSum(nums, target))

#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#


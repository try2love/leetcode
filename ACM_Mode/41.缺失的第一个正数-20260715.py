#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30404
#
# [41] 缺失的第一个正数
# 12:46 ACM AC
from typing import List
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 参考答案
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
        
        n = len(nums)
        for idx in range(n):
            while nums[idx] <= n and nums[idx] > 0 and nums[idx]!=(idx+1) and nums[idx] != nums[nums[idx]-1]:
                x = nums[idx]
                nums[x-1], nums[idx] = nums[idx], nums[x-1]
        for idx in range(len(nums)):
            if nums[idx] != (idx+1):
                return idx+1
        return n+1

# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.firstMissingPositive(nums))

#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#


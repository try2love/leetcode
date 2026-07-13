#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30404
#
# [283] 移动零
# 4:02 ACM AC
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i0 = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1
        return

        stack_size = 0
        for x in nums:
            if x:
                nums[stack_size] = x
                stack_size += 1
        nums[stack_size:] = [0] * (len(nums)- stack_size)
        return

        stack_size = 0
        for x in nums:
            if x:
                nums[stack_size] = x
                stack_size += 1
        for i in range(stack_size, len(nums)):
            nums[i] = 0
        return

        # 一眼双指针
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        while slow < fast:
            nums[slow] = 0
            slow += 1
        return
        
# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
sol.moveZeroes(nums)
print(nums)


#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


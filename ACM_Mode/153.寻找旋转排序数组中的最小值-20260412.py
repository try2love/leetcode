#
# @lc app=leetcode.cn id=153 lang=python3
# @lcpr version=30403
#
# [153] 寻找旋转排序数组中的最小值
# 9:27 ACM AC，还是对这种问题的解法不够熟练
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分找中点位置
        if not nums:
            return -1
        if nums[0] <= nums[-1]:
            return nums[0]
        left, right = 0, len(nums) # 左闭右开
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= nums[0]:
                left = mid+1
            else:
                right = mid
        return nums[left]

# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.findMin(nums))

#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,15,17]\n
# @lcpr case=end

#


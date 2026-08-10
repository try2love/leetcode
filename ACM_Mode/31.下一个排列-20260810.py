#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30404
#
# [31] 下一个排列
# 8:16直接看答案
from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从前往后单调递增，则交换最后两个
        # 从后往前单调不减，则reverse
        # 先增后减，则
        # 参考
        n = len(nums)
        i = n-2
        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1
        if i>=0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#


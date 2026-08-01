#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30404
#
# [33] 搜索旋转排序数组
# 15:27 错误，看答案
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        # cankao
        while left < right:
            mid = (left+right)//2
            x = nums[mid]
            if target > nums[-1] >= x:
                # target在第一段，x在第二段
                right = mid
            elif x > nums[-1] >= target:
                # target第二段，mid第一段
                left = mid+1
            elif x >= target:
                # 在同意段
                right = mid
            else:
                left = mid+1
        return left if nums[left]==target else -1

        while left < right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[mid] >= nums[left] and nums[left] <= target:
                    # mid在左半边
                    right = mid
                elif nums[mid] >= nums[left] and nums[left] > target:
                    left = mid+1
                else:
                    right = mid
            else:
                if nums[mid] >= nums[right-1]:
                    left = mid + 1
                else:
                    right = mid
        if left >= len(nums):
            return -1
        if nums[left]!=target:
            return -1
        return left
# @lc code=end



#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#


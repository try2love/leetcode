#
# @lc app=leetcode.cn id=35 lang=python3
# @lcpr version=30404
#
# [35] 搜索插入位置
# 1:04 ACM AC，使用函数库
# 1:56 ACM AC，手写
from typing import List
from bisect import bisect_left
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分
        # return bisect_left(nums, target)
        left, right = 0, len(nums) # 左闭右开
        while left < right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return left
        
# @lc code=end



#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30404
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
# 3：46 ACM AC
from typing import List
from bisect import bisect_left, bisect_right
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, right-1]
        
# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#


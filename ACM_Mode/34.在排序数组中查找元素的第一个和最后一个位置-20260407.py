#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30403
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
# 4:48 ACM AC，使用了库函数 4:35 手写二分成功
from typing import List
# @lc code=start
from bisect import bisect_left, bisect_right
class Solution:
    def lower_bound(self, nums: List[int], target:int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # -----参考答案------
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = self.lower_bound(nums, target+1)-1
        return [start, end]
        # -----参考答案------

        # 自定义二分
        left, right = 0, len(nums) # 左闭右开
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if left >= len(nums) or nums[left]!=target:
            return [-1, -1]
        ans_left = left
        left, right = 0, len(nums) # 左闭右开
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] <= target:
                left = mid + 1
        return [ans_left, left-1]

        return [-1, -1] if bisect_left(nums, target)>=len(nums) or nums[bisect_left(nums, target)]!=target else [bisect_left(nums, target), bisect_right(nums, target)-1]

# @lc code=end
import sys
import json
nums = json.loads(sys.stdin.readline().strip())
target = eval(input())
sol = Solution()
print(sol.searchRange(nums, target))


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


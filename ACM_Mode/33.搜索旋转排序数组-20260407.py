#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30403
#
# [33] 搜索旋转排序数组
# 15:13，先找中间再左右的方法； 19:42没有实现一次二分
from typing import List
from bisect import bisect_left
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # -----参考答案------
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right)//2
            x = nums[mid]
            if target > nums[-1] >= x: # target在第一段，x在第二段
                right = mid
            elif x > nums[-1] >= target: # x在第一段，target在第二段
                left = mid + 1
            elif x >= target: # 在同一段，直接二分
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1
        # -----参考答案------
        
        # 尝试一次二分，失败
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid] < target:
                left = mid + 1
            elif nums[right-1] >= nums[mid] > target:
                right = mid
        return -1 if left>=n or nums[left]!=target else left

        # 先找分界线
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid+1
        # return mid, nums[mid] # 找到了
        idx = bisect_left(nums[left:], target)
        tmp_right =  -1 if idx+left >= n or nums[idx+left]!=target else idx+left
        idx = bisect_left(nums[:left], target)
        tmp_left =  -1 if nums[idx]!=target else idx
        return max(tmp_left, tmp_right)

# @lc code=end
import sys
import json
nums = json.loads(sys.stdin.readline().strip())
target = eval(input())
sol = Solution()
print(sol.search(nums, target))


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


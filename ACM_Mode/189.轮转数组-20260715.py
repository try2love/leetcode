#
# @lc app=leetcode.cn id=189 lang=python3
# @lcpr version=30404
#
# [189] 轮转数组
# 5:29 ACM AC
from typing import List
# @lc code=start
class Solution:
    def reverse(self, nums: List[int], start:int, end:int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 参考答案
        def reverse(i:int, j:int) -> None:
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        n = len(nums)
        k %= n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        return

        # 后k个原地旋转；前面的也原地旋转，然后整体原地选装
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-k-1)
        self.reverse(nums, len(nums)-k, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
        
# @lc code=end
import json
import sys
nums = json.loads(sys.stdin.readline().strip())
k = eval(input())
sol = Solution()
sol.rotate(nums, k)
print(nums)


#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-1,-100,3,99]\n2\n
# @lcpr case=end

#


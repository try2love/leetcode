#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30403
#
# [31] 下一个排列
# 18:22 ACM AC
from typing import List
# @lc code=start
class Solution:
    def reverse(self, nums:List[int], start:int, end:int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        # -----参考答案------
        n = len(nums)
        i = n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i -= 1
        if i>=0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j],nums[i]
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return
        # -----参考答案------

        # 如果逆向读取一直非递减，那么就全部逆转
        # 1231->1312 逆向读取到第一个递减，置换后面第一个比他大的，后续全部逆转
        # 1232321->1233221 -> 1233112; 13221->23211->21123
        end = nums[-1]
        idx = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < end:
                idx = i
                break
            end = nums[i]
        if idx == -1:
            self.reverse(nums, 0, len(nums)-1)
            return
        for j in range(len(nums)-1, idx, -1):
            if nums[j] > nums[idx]:
                nums[idx], nums[j] = nums[j], nums[idx]
                self.reverse(nums, idx+1, len(nums)-1)
                break
        return
# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
sol.nextPermutation(nums)
print(nums)

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


#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30404
#
# [75] 颜色分类
# 7:26 ACM AC开辟了额外空间
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 参考答案
        p0 = p1 = 0
        for i,x in enumerate(nums):
            nums[i] = 2
            if x <= 1:
                nums[p1] = 1
                p1 += 1
            if x == 0:
                nums[p0] = 0
                p0 += 1
        return

        cnt = Counter(nums)
        for i in range(len(nums)):
            if cnt[0]>0:
                nums[i] = 0
                cnt[0] -= 1
            elif cnt[1]>0:
                nums[i] = 1
                cnt[1] -= 1
            else:
                nums[i] = 2
                cnt[2] -= 1
        # left, right = 0, len(nums)-1
        # while left < right:
        #     while right >=0 and nums[right] == 2:
        #         right -= 1
        #     while left < len(nums) and nums[left] == 0:
        #         left += 1
        #     nums[left], nums[right] = nums[right], nums[left]
        #     if nums[left] == 0:
        #         left += 1
        #     right -= 1
        
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#


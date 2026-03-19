#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30400
#
# [283] 移动零
# 用时7:07 ACM AC
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 统计0的个数即可
        time = 0
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] == 0:
                time += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
        return


# @lc code=end

import sys
data = list(map(int,sys.stdin.readline().strip().split()))
sol = Solution()
sol.moveZeroes(data)
print(data)

#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30401
#
# [55] 跳跃游戏
# 没有考虑到初始可能为0的情况
# 修改后，3:51 AC, 4:51 ACM AC
from typing import List
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 只关注能不能跳到，所以是一个贪心的问题
        right_max = nums[0]
        for idx in range(len(nums)-1):
            if idx > right_max:
                return False
            right_max = max(right_max, idx+nums[idx])
        return  right_max>=len(nums)-1
# @lc code=end

import sys
nums = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.canJump(nums))


#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#


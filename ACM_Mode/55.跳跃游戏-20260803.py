#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30404
#
# [55] 跳跃游戏
# 2:49 ACM AC
from typing import List
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 维护右侧最大边界
        right = 0
        for idx, x in enumerate(nums):
            if idx > right:
                return False
            right = max(right, idx+x)
        return right >= len(nums)-1
        
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#


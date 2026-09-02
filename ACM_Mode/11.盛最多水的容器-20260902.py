#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30404
#
# [11] 盛最多水的容器
# 3:48 ACM AC
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        ans = 0
        while left <= right:
            ans = max(ans, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
            
# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#


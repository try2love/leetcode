#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30404
#
# [42] 接雨水
# 5:13 ACM AC
from typing import List
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 两个数组，一个记录左侧最高，一个记录右侧最高
        n = len(height)
        ans = 0
        left = [0] * n
        right = [0] * n
        for i in range(1, n):
            left[i] = max(height[i-1], left[i-1])
        for i in range(n-2, -1, -1):
            right[i] = max(height[i+1], right[i+1])
        for i, h in enumerate(height):
            ans += max((min(left[i], right[i]) - h),0)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#


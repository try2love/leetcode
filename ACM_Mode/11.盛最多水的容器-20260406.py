#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30402
#
# [11] 盛最多水的容器
# 3:55 ACM AC
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 应该是双指针
        left, right = 0, len(height) - 1 # 闭区间
        ans = 0
        while left <= right:
            ans = max(ans, min(height[right], height[left]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans

# @lc code=end
import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.maxArea(nums))

#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#


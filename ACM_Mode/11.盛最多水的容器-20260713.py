#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30404
#
# [11] 盛最多水的容器
# 3:57 ACM AC
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 双指针两头掐
        left, right = 0, len(height)-1
        if left == right:
            return 0
        ans = 0
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

# @lc code=end

import sys
import json
height = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.maxArea(height))

#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#


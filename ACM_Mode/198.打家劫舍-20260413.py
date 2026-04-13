#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30403
#
# [198] 打家劫舍
# 2:35记忆化搜索, 3:29一维dp, 4:24两个临时变量实现
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0
        for i in range(len(nums)):
            f0, f1 = max(f0, f1+nums[i]), f0
        return f0

        dp = [0]*(len(nums)+2)
        for i in range(len(nums)):
            dp[i+2] = max(dp[i+1], dp[i]+nums[i])
        return dp[-1]

        @cache
        def dfs(i:int):
            if i<0:
                return 0
            return max(dfs(i-1), dfs(i-2)+nums[i])
        return dfs(len(nums)-1)

# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.rob(nums))

#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#


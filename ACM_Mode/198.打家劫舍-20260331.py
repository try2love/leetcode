#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30402
#
# [198] 打家劫舍
# 2:36 ACM AC 0:51转dp
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # -----参考答案------
        # 空间优化
        f0 = f1 = 0
        for i in range(len(nums)):
            f1, f0 = max(f1, f0+nums[i]), f1
        return f1
        # -----参考答案------

        n = len(nums)
        dp = [0] * (n+2)
        for i in range(n):
            dp[i+2] = max(dp[i+1], dp[i] + nums[i])
        return dp[n+1]

        @cache
        def dfs(i:int):
            if i< 0 :
                return 0
            return max(dfs(i-1), dfs(i-2)+nums[i])
        return dfs(len(nums)-1)

# @lc code=end
import sys
data = list(map(int, sys.stdin.readline().strip().split())
sol = Solution()
print(sol.rob(data))

#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#


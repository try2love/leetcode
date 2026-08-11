#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30404
#
# [198] 打家劫舍
# 2:13 ACM AC 3:03 一维 3:53 空间优化 
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f0, f1 = 0, 0
        for i in range(n):
            f0, f1 = f1, max(f1, f0+nums[i])
        return f1

        dp = [0] * (n+2)
        for i in range(n):
            dp[i+2] = max(dp[i+1], dp[i] + nums[i])
        return dp[n+1]

        @cache
        def dfs(i:int):
            if i<0:
                return 0
            return max(dfs(i-1), dfs(i-2)+nums[i])
        return dfs(n-1)
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30404
#
# [198] 打家劫舍
# 2:03 记忆化搜索 6:18 一维dp 8:06 循环数组
# o1空间写错了
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 参考
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f1, f0+x)
        return f1

        @cache
        def dfs(i:int) -> int:
            if i<0:
                return 0
            return max(dfs(i-1), dfs(i-2)+nums[i])
        return dfs(len(nums)-1)

        # 错误
        f0, f1, f2 = 0, 0, 0
        for i in range(len(nums)):
            f0, f1, f2 = f1, f2, max(f0, f1+nums[i])
        return f2

        dp = [0] * 3
        for i in range(len(nums)):
            dp[(i+2)%3] = max(dp[(i+1)%3], dp[i%3]+nums[i])
        return dp[(len(nums)+1)%3]

        dp = [0]*(len(nums)+2)
        for i in range(len(nums)):
            dp[i+2] = max(dp[i+1], dp[i]+nums[i])
        return dp[-1]

        # @cache
        # def dfs(i:int):
        #     if i<0:
        #         return 0
        #     return max(dfs(i-1), dfs(i-2)+nums[i])
        # return dfs(len(nums)-1)
        #     if i>=len(nums):
        #         return 0
        #     return max(dfs(i+1), dfs(i+2)+nums[i])
        # return dfs(0)
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#


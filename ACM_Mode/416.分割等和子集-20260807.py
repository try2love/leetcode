#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30404
#
# [416] 分割等和子集
# 5:14 ACM AC 9:22 DP AC 10:30减少空间AC 12:32一维DP
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        dp = [False]*(total//2+1)
        for i,x in enumerate(nums):
            dp[0] = True
            for j in range(total//2, -1, -1):
                if x <= j:
                    dp[j] = dp[j] or dp[j-x]
        return dp[-1]
        
        dp = [[False]*(total//2+1) for _ in range(2)]
        for i,x in enumerate(nums):
            dp[i%2][0] = True
            for j in range(total//2+1):
                if x > j:
                    dp[(i+1)%2][j] = dp[i%2][j]
                else:
                    dp[(i+1)%2][j] = dp[i%2][j-x] or dp[i%2][j]
        return dp[(len(nums))%2][total//2]
        
        dp = [[False]*(total//2+1) for _ in range(len(nums)+1)]
        for i,x in enumerate(nums):
            dp[i][0] = True
            for j in range(total//2+1):
                if x > j:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j-x] or dp[i][j]
        return dp[len(nums)][total//2]
        
        @cache
        def dfs(i:int, target:int):
            if target == 0:
                return True
            if i<0:
                return False
            if nums[i] > target:
                return dfs(i-1, target)
            return dfs(i-1, target-nums[i]) or dfs(i-1, target)
        return dfs(len(nums)-1,total//2)
        
# @lc code=end



#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#


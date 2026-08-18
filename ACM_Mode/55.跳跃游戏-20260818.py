#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30404
#
# [55] 跳跃游戏
# 5:17 超时 8:42 ACM AC
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 参考
        mx = 0
        for i, jump in enumerate(nums):
            if i>mx:
                return False
            mx = max(mx, i+jump)
            if mx >= len(nums)-1:
                return True

        mx = 0
        for i, jump in enumerate(nums):
            if i > mx:
                return False
            mx = max(mx, i+jump)
        return True

        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i,x in enumerate(nums):
            if dp[i]:
                for j in range(1, x+1):
                    if i+j >= n-1:
                        return True
                    dp[i+j] = True
        return dp[-1]

        @cache
        def dfs(i:int):
            if i>=n-1:
                return True
            return any([dfs(i+x) for x in range(nums[i], 0, -1)])
        return dfs(0)
        
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#


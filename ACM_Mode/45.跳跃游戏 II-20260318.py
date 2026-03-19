#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30400
#
# [45] 跳跃游戏 II
# 6:59  实现记忆化搜索的ACM AC
from typing import List
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 最优解：贪心
        ans = 0
        cur_right = 0
        next_right = 0
        for i in range(len(nums)-1):
            next_right = max(next_right, i + nums[i])
            if i == cur_right:
                cur_right = next_right
                ans += 1
        return ans

        # dp = [inf]*(len(nums))
        # dp[0] = 0
        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         if j+nums[j]>=i:
        #             dp[i] = min(dp[i], dp[j] + 1)
        # return dp[len(nums)-1]

        # @cache
        # def dfs(i:int):
        #     nonlocal ans
        #     if i<=0:
        #         return 0
        #     for j in range(i-1,-1,-1):
        #         if j+nums[j]>=i:
        #             ans = min(ans, dfs(j)+1)
        #     return ans
        # return dfs(len(nums)-1)
# @lc code=end

import sys
data = list(map(int,sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.jump(data))

#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30402
#
# [122] 买卖股票的最佳时机 II
# 9:45 ACM AC; 2:39 二维dp 1:18 一维dp
from typing import List
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*2
        dp[1] = -inf
        for i in range(n):
            dp[0], dp[1] = max(dp[1]+prices[i], dp[0]), max(dp[1], dp[0] - prices[i])
        return dp[0]

        # dp = [[0]*2 for _ in range(n+1)]
        # dp[0][1] = -inf
        # for i in range(n):
        #     dp[i+1][1] = max(dp[i][1], dp[i][0] - prices[i])
        #     dp[i+1][0] = max(dp[i][1]+prices[i], dp[i][0])
        # return dp[n][0]

        # @cache
        # def dfs(i:int, hold:bool):
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i-1, hold), dfs(i-1, False)-prices[i])
        #     return max(dfs(i-1, True)+prices[i], dfs(i-1, False))
        # return dfs(len(prices)-1, False)
    
# @lc code=end
import sys
prices = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.maxProfit(prices))

#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#


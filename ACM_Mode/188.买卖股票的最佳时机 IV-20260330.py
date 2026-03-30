#
# @lc app=leetcode.cn id=188 lang=python3
# @lcpr version=30402
#
# [188] 买卖股票的最佳时机 IV
# 11:24 ACM AC 记忆化搜索 5:04 三位dp 0:58 二维dp
from typing import List
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*(k+2) for _ in range(2)]
        dp[1] = [-inf]*(k+2)
        for i in range(n):
            dp[1][k+1] = -inf
            for time in range(k+1):
                dp[1][time] = max(dp[1][time], dp[0][time]-prices[i])
                dp[0][time] = max(dp[1][time+1]+prices[i], dp[0][time])
        return dp[0][0]


        dp = [[[0]*(k+2) for _ in range(2)] for _ in range(n+1)]
        dp[0][1] = [-inf]*(k+2)
        for i in range(n):
            dp[i][1][k+1] = -inf
            for time in range(k+1):
                dp[i+1][1][time] = max(dp[i][1][time], dp[i][0][time]-prices[i])
                dp[i+1][0][time] = max(dp[i][1][time+1]+prices[i], dp[i][0][time])
        return dp[n][0][0]

        @cache
        def dfs(i:int, time:int, hold:bool):
            if i<0 or time > k:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, time, True), dfs(i-1, time, False)-prices[i])
            return max(dfs(i-1, time+1, True)+prices[i], dfs(i-1, time, False))
        return dfs(n-1, 0, False)
        
# @lc code=end
import sys
k = eval(input())
prices = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.maxProfit(k, prices))


#
# @lcpr case=start
# 2\n[2,4,1]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[3,2,6,5,0,3]\n
# @lcpr case=end

#


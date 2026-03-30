#
# @lc app=leetcode.cn id=714 lang=python3
# @lcpr version=30402
#
# [714] 买卖股票的最佳时机含手续费
# 5:31 ACM AC 1:42 二维dp 1:25，两个常量AC
from typing import List
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        f0, f1 = 0, -inf
        for i in range(n):
            f1, f0 = max(f1,f0-prices[i]), max(f1+prices[i]-fee,f0)
        return f0

        dp = [[0]*2 for _ in range(n+1)]
        dp[0][1] = -inf
        for i in range(n):
            dp[i+1][1] = max(dp[i][1], dp[i][0]-prices[i])
            dp[i+1][0] = max(dp[i][1]+prices[i]-fee, dp[i][0])
        return dp[n][0]

        @cache
        def dfs(i:int, hold:bool):
            if i<0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True), dfs(i-1, False)-prices[i])
            return max(dfs(i-1, True)+prices[i]-fee, dfs(i-1,False))
        return dfs(n-1, False)


# @lc code=end
import sys
prices = list(map(int, sys.stdin.readline().strip().split()))
fee = eval(input())
sol = Solution()
print(sol.maxProfit(prices, fee))

#
# @lcpr case=start
# [1,3,2,8,4,9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,7,5,10,3]\n3\n
# @lcpr case=end

#


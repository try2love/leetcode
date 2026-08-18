#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30404
#
# [122] 买卖股票的最佳时机 II
# 6:49 ACM AC，想不出来DP做法
from typing import List
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # cankao
        f0, f1 = 0, -inf
        for p in prices:
            f0, f1 = max(f0, f1+p), max(f1, f0-p)
        return f0

        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]
        dp[0][1] = -inf
        for i, p in enumerate(prices):
            dp[i+1][0] = max(dp[i][0], dp[i][1]+p)
            dp[i+1][1] = max(dp[i][1], dp[i][0] - p)
        return dp[n][0]

        @cache
        def dfs(i:int, hold:bool) -> int:
            if i<0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, True),dfs(i-1,False)-prices[i])
            return max(dfs(i-1, False), dfs(i-1, True)+prices[i])
        return dfs(len(prices)-1, False)

        # 状态：持有，卖出
        n = len(prices)
        @cache
        def dfs(i:int, hold:bool):
            if i>=n:
                return -inf if hold else 0
            if hold: # 当前持有，可以卖可以继续持有
                return max(dfs(i+1, False)+prices[i], dfs(i+1, True))
            else: # 当前没有，可以不买也可以买
                return max(dfs(i+1, True)-prices[i], dfs(i+1, False))
        return max([dfs(i, False) for i in range(n)])
        
# @lc code=end



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


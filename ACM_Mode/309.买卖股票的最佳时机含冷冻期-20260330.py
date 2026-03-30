#
# @lc app=leetcode.cn id=309 lang=python3
# @lcpr version=30402
#
# [309] 买卖股票的最佳时机含冷冻期
# 16:50没做出来。 看了参考答案，发现确实如此，没有必要维护一个chill
from typing import List
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # -----参考答案------
        pre0 = 0
        f0 = 0
        f1 = -inf
        for i in range(n):
            f1, f0, pre0 = max(f1, pre0-prices[i]), max(f0, f1+prices[i]), f0
        return f0

        dp = [[0]*2 for _ in range(n+2)]
        dp[0][1] = dp[1][1] = -inf
        for i in range(n):
            dp[i+2][1] = max(dp[i+1][1], dp[i][0]-prices[i])
            dp[i+2][0] = max(dp[i+1][0], dp[i+1][1]+prices[i])
        return dp[-1][0]

        @cache
        def dfs(i:int, hold:bool) -> int:
            if i<0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1,True), dfs(i-2, False)-prices[i])
            return max(dfs(i-1, False), dfs(i-1, True)+prices[i])
        return dfs(n-1, False)
        # -----参考答案------

        # 下面的做法是错误的，a不出来
        @cache
        def dfs(i:int, hold:bool, chill:bool):
            if i<0:
                return -inf if hold else 0
            if chill and i>0:
                return dfs(i-1, False, False)+prices[i-1] if not hold else -inf
            if hold:
                return max(dfs(i-1, True, False), dfs(i-1, False, True)-prices[i], dfs(i-1, False, False)-prices[i])
            # 一定是卖出后，持有为False，才可能是冷静期
            # 当前chill为False， hold为False
            return max(dfs(i-1, False, True), dfs(i-1, False, False))
        return max(dfs(n-1, False, False), dfs(n-1, False, True))

# @lc code=end

import sys
prices = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()


#
# @lcpr case=start
# [1,2,3,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


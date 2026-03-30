#
# @lc app=leetcode.cn id=123 lang=python3
# @lcpr version=30402
#
# [123] 买卖股票的最佳时机 III
# 22:41 记忆化搜索爆存储；dp结果错误。修改了一下，三维dp通过，第一版错因在于对k设定了长度3，而不是4
# 长度4， 可以包括0，1，2，3，其中最后一种是越界。
from typing import List
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*4 for _ in range(2)]
        dp[1] = [-inf] * 4
        for i in range(n):
            dp[1][3] = -inf
            for time in range(3):
                dp[1][time] = max(dp[1][time], dp[0][time]-prices[i])
                dp[0][time] = max(dp[1][time+1]+prices[i], dp[0][time])
        return dp[0][0]
                

        dp = [[[0]*4 for _ in range(2)] for _ in range(n+1)]
        dp[0][1] = [-inf] * 4
        for i in range(n):
            dp[i][1][3] = -inf
            for time in range(3):
                dp[i+1][1][time] = max(dp[i][1][time], dp[i][0][time]-prices[i])
                dp[i+1][0][time] = max(dp[i][1][time+1]+prices[i], dp[i][0][time])
        return dp[n][0][0]
                

        # 666 存储爆了
        if not prices:
            return 0
        @cache
        def dfs(i:int, hold:bool, times:int):
            # 倒着排序，times在一次卖出后+1， hold无法买入
            if i<0 or times>2:
                return -inf if hold else 0
            if hold:
                return max(dfs(i-1, hold, times), dfs(i-1, False, times)-prices[i])
            return max(dfs(i-1, True, times+1)+prices[i], dfs(i-1,False,times))
        return dfs(len(prices)-1, False, 0)
# @lc code=end
import sys
prices = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.maxProfit(prices))

#
# @lcpr case=start
# [3,3,5,0,0,3,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#


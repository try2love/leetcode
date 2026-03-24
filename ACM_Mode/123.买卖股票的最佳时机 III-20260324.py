#
# @lc app=leetcode.cn id=123 lang=python3
# @lcpr version=30401
#
# [123] 买卖股票的最佳时机 III
# 12:18 核心 AC 13:32 ACM AC
from typing import List
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # -----参考答案------
        k = 2
        dp = [[-inf]*2 for _ in range(k+2)]
        for j in range(1, k+2):
            dp[j][0] = 0
        for p in prices:
            for j in range(k+1, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1]+p)
                dp[j][1] = max(dp[j][1], dp[j-1][0]-p)
        return dp[-1][0]
        # -----参考答案------

        # @cache
        # def dfs(i:int, hold:bool, times:int):
        #     if i>=n or times<=0:
        #         return -inf if hold else 0
        #     if hold:
        #         # 可以持续hold，可以卖出
        #         return max(dfs(i+1, hold, times), dfs(i+1, False, times-1)+prices[i])
        #     return max(dfs(i, True, times)-prices[i], dfs(i+1, False, times))
        # return max(dfs(0,0,2), dfs(0,1,2)-prices[0])

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


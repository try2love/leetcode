#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30401
#
# [322] 零钱兑换
# 5:47 记忆化搜索 额外10:26，二维dp 额外3:10，一维dp
from typing import List
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 一维动态规划
        dp = [inf]*(amount+1)
        for i in range(len(coins)):
            dp[0] = 0
            for j in range(amount):
                if j+1 >= coins[i]:
                    dp[j+1] = min(dp[j+1-coins[i]]+1, dp[j+1])
                else:
                    dp[j+1] = dp[j+1]
        return dp[-1] if dp[-1] < inf else -1

        # # 二维动态规划
        # dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        # dp[0] = [inf]*(amount+1)
        # for i in range(len(coins)):
        #     for j in range(amount):
        #         if j+1 >= coins[i]:
        #             dp[i+1][j+1] = min(dp[i+1][j+1-coins[i]]+1, dp[i][j+1])
        #         else:
        #             dp[i+1][j+1] = dp[i][j+1]
        # return dp[-1][-1] if dp[-1][-1] < inf else -1

        # # 记忆化搜索
        # @cache
        # def dfs(i:int, left:int):
        #     if i<0:
        #         return inf
        #     if left == 0:
        #         return 0
        #     if left >= coins[i]:
        #         return min(dfs(i, left-coins[i])+1, dfs(i-1,left))
        #     return dfs(i-1, left)
        # ans = dfs(len(coins)-1, amount)
        # return ans if ans < inf else -1

# @lc code=end
import sys
coins = list(map(int, sys.stdin.readline().strip().split()))
amount = eval(input())
sol = Solution()
print(sol.coinChange(coins, amount))


#
# @lcpr case=start
# [1,2,5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#


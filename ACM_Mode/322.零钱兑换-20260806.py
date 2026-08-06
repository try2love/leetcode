#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30404
#
# [322] 零钱兑换
# 6:16 记忆化搜索 14:00 dp错误
from collections import List
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 参考
        f = [0] + [inf]*amount
        for x in coins:
            for c in range(x, amount+1):
                f[c] = min(f[c], f[c-x]+1)
        ans = f[amount]
        return ans if ans<inf else -1

        n = len(coins)
        f = [[inf] * (amount+1) for _ in range(2)]
        f[0][0] = 0
        for i,x in enumerate(coins):
            for j in range(amount+1):
                if j<x:
                    f[(i+1)%2][j] = f[i%2][j]
                else:
                    f[(i+1)%2][j] = min(f[i%2][j], f[(i+1)%2][j-x]+1)
        ans = f[n%2][amount]
        return ans if ans<inf else -1

        n = len(coins)
        f = [[inf]*(amount+1) for _ in range(n+1)]
        f[0][0] = 0
        for i,x in enumerate(coins):
            for c in range(amount+1):
                if c<x:
                    f[i+1][c] = f[i][c]
                else:
                    f[i+1][c] = min(f[i][c], f[i+1][c-x]+1)
        ans = f[n][amount]
        return ans if ans<inf else -1

        @cache
        def dfs(i:int, c:int) -> int:
            if i<0:
                return 0 if c==0 else inf
            if c<coins[i]:
                return dfs(i-1, c)
            return min(dfs(i-1,c), dfs(i,c-coins[i])+1)
        ans = dfs(len(coins)-1, amount)
        return ans if ans<inf else -1

        dp = [[inf] * (amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 0
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[i+1][j] = min(dp[i][j],dp[i+1][j-coins[i]]+1)
        print(dp)
        return dp[len(coins)][amount] if dp[len(coins)][amount] < inf else -1


        @cache
        def dfs(i:int, target:int) -> int:
            if i<0 or target < 0:
                return inf
            if target==0:
                return 0
            if target < coins[i]:
                return dfs(i-1, target)
            return min(dfs(i, target-coins[i])+1, dfs(i-1, target))
        ans = dfs(len(coins)-1, amount)
        return ans if ans < inf else -1
# @lc code=end



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


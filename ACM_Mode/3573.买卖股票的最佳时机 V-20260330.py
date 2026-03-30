#
# @lc app=leetcode.cn id=3573 lang=python3
# @lcpr version=30402
#
# [3573] 买卖股票的最佳时机 V
#
from typing import List
from math import inf
from functools import cache
# @lc code=start
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        @cache
        def dfs(i:int, hold:int, time:int):
            # hold：1持有，0没有 -1 做空
            if i<0 or time<0:
                return -inf if hold!=0 else 0
            if hold==1:
                # 持有
                return max(dfs(i-1, 1,time), dfs(i-1, 0,time)-prices[i])
            elif hold == 0:
                # 没有
                return max(dfs(i-1, 0, time), dfs(i-1,1, time-1)+prices[i], dfs(i-1, -1, time-1)-prices[i])
            else:
                # 做空
                return max(dfs(i-1, 0, time)+prices[i], dfs(i-1,-1, time))
        return dfs(n-1, 0,k)
# @lc code=end



#
# @lcpr case=start
# [1,7,9,8,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [12,16,19,19,8,1,19,13,9]\n3\n
# @lcpr case=end

#


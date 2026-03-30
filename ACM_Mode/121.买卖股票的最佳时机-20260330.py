#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30402
#
# [121] 买卖股票的最佳时机
# 4:50 ACM AC
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # -----参考答案------
        ans = 0
        min_price = prices[0]
        for p in prices:
            ans = max(ans, p - min_price)
            min_price = min(min_price, p)
        return ans
        # -----参考答案------

        if not prices:
            return 0
        buy = sell = prices[0]
        ans = 0
        for x in prices:
            if x < buy:
                ans = max(ans, sell-buy)
                buy = x
                sell = x
            else:
                sell = max(sell, x)
        return max(ans, sell - buy)

# @lc code=end
import sys
nums = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.maxProfit(nums))


#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#


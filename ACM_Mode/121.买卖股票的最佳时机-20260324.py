#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30401
#
# [121] 买卖股票的最佳时机
# 5:29 ACM AC，但是为什么不维护ans，答案就是错误的呢，因为把6弹出了
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # -----参考答案------
        # 闹麻了，还单调栈呢
        cur = prices[0]
        ans = 0
        for p in prices:
            ans = max(ans, p-cur)
            if p < cur:
                cur = p
        return ans
        # -----参考答案------
        
        # # 一眼单调栈，单调递增栈
        # if not prices:
        #     return 0
        # st = [prices[0]]
        # ans = 0
        # for i in range(1,len(prices)):
        #     while st and prices[i]<st[-1]:
        #         st.pop()
        #     st.append(prices[i])
        #     ans = max(ans, prices[i]-st[0])
        # return ans
        
# @lc code=end
import sys
prices = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.maxProfit(prices))


#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#


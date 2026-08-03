#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30404
#
# [121] 买卖股票的最佳时机
# 6:24 ACM AC
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 参考答案
        ans = 0
        min_price = prices[0]
        for p in prices:
            ans = max(ans, p-min_price)
            min_price = min(min_price, p)
        return ans

        # 感觉是一个单调递增栈
        st = []
        ans = 0
        for i,x in enumerate(prices):
            while len(st):
                if prices[st[-1]] > x:
                    ans = max(ans, prices[st[-1]]-prices[st[0]])
                    st.pop()
                else:
                    break
            st.append(i)
        return max(ans, prices[st[-1]]-prices[st[0]]) if len(st) else ans
        
# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30404
#
# [121] 买卖股票的最佳时机
# 4:41 ACM aC
from collections import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        # 贪心
        cur = prices[0]
        for x in prices[1:]:
            if cur > x:
                cur = x
            else:
                ans = max(ans, x - cur)
        return ans

        # 单调递增栈
        st = []
        for i,x in enumerate(prices):
            while st and prices[st[-1]] > x:
                tmp = st.pop()
                if st:
                    ans = max(prices[tmp] - prices[st[0]], ans)
            st.append(i)
        return max(ans, prices[st[-1]]-prices[st[0]]) if st else ans

# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#


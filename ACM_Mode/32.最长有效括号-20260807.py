#
# @lc app=leetcode.cn id=32 lang=python3
# @lcpr version=30404
#
# [32] 最长有效括号
# 5:20 没有思路，直接看答案

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # -----参考答案------
        n = len(s)
        if n==0:
            return 0
        dp = [0] * (n+1)
        st = [] # 存左括号位置
        for i,c in enumerate(s):
            if c == '(':
                st.append(i)
            elif len(st) > 0:
                top = st[-1]
                st.pop()
                dp[i] = i-top+1+(dp[top-1] if top >=1 else 0)
        return max(dp)

        st = [-1] # 虚拟红线哨兵
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)
            elif len(st) > 1:
                st.pop()
                ans = max(ans, i-st[-1]) # 右端点为i时，左端点最小值为st[-1]
            else: # 栈只有一个数，是红线，s[i]成为新的红线
                st[0] = i
        return ans
        # -----参考答案------

        # ans = 0
        # left = right = 0
        # for i, x in enumerate(s):

        
# @lc code=end



#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

#


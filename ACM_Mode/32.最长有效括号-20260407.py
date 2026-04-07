#
# @lc app=leetcode.cn id=32 lang=python3
# @lcpr version=30403
#
# [32] 最长有效括号
# 22:00 没做出来，看答案。
from collections import defaultdict
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
            else: # 栈只有一个数，是红线，s[i]成为新的红线，不管是左括号还是右括号
                st[0] = i
        return ans
        # -----参考答案------

        # 双指针，遇到多余的右括号才移动左指针
        # 错误case："()(()"，输出了4而不是2
        if len(s) == 0:
            return 0
        left = right = ans = 0
        cnt = defaultdict(int)
        while right < len(s):
            if s[right] == ")":
                cnt[s[right]] += 1
                right += 1
                ans = max(ans, min(cnt["("], cnt[")"])*2)
                while cnt["("] < cnt[")"] and left < right:
                    cnt[s[left]] -= 1
                    left += 1
            else:
                # 左括号
                cnt["("] += 1
                right += 1
        return ans
    
# @lc code=end
s = input()
sol = Solution()
print(sol.longestValidParentheses(s))


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


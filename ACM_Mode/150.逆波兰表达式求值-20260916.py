#
# @lc app=leetcode.cn id=150 lang=python3
# @lcpr version=30404
#
# [150] 逆波兰表达式求值
# 8:55 错误，主要是 “两个整数之间的除法总是 向零截断 。”怎么表达
from typing import List
from math import trunc
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 参考答案
        st = []
        for token in tokens:
            if len(token) > 1 or token[0].isdigit():
                st.append(int(token))
                continue
            x = st.pop()
            if token == '+':
                st[-1] += x
            elif token == '-':
                st[-1] -= x
            elif token == '*':
                st[-1] *= x
            else:
                # st[-1] = trunc(st[-1]/x)
                y = st[-1]
                st[-1] = y // x if y * x >= 0 else -(-y // x)
        return st[0]

        st = []
        for x in tokens:
            if x not in ['+', '-', '*', '/']:
                st.append(int(x))
            else:
                b = st.pop()
                a = st.pop()
                if x == '+':
                    st.append(a+b)
                elif x == '-':
                    st.append(a-b)
                elif x == '*':
                    st.append(a*b)
                else:
                    if a%b >= 0:
                        st.append(a//b)
                    else:
                        st.append(0)
        return st[0]
        
# @lc code=end
tokens = ["4","-2","/","2","-3","-","-"]
sol = Solution()
print(sol.evalRPN(tokens))


#
# @lcpr case=start
# ["2","1","+","3","*"]\n
# @lcpr case=end

# @lcpr case=start
# ["4","13","5","/","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]\n
# @lcpr case=end

#


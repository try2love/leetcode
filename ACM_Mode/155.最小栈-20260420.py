#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30403
#
# [155] 最小栈
# 2:24 ACM AC
from math import inf
# @lc code=start
class MinStack:

    def __init__(self):
        self.st = [(-1,inf)]

    def push(self, val: int) -> None:
        self.st.append((val, min(self.st[-1][1], val)))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end



#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#


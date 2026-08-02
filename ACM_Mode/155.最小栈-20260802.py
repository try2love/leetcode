#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30404
#
# [155] 最小栈
# 3:08 没有好的常数时间获取最小元素的方案
from math import inf
# @lc code=start
class MinStack:
    def __init__(self):
        self.st = [(0, inf)]

    def push(self, val: int) -> None:
        self.st.append((val, min(self.st[-1][1], val)))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]

class MinStack:
    def __init__(self):
        self.st = []
        self.mn = inf
    def push(self, val:int) -> None:
        self.st.append(val-self.mn)
        self.mn = min(self.mn, val)
    def pop(self) -> None:
        self.mn -= min(self.st.pop(), 0)
    def top(self) -> int:
        return self.mn + max(self.st[-1], 0)
    def getMin(self) -> int:
        return self.mn

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


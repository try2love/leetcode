#
# @lc app=leetcode.cn id=155 lang=python3
# @lcpr version=30400
#
# [155] 最小栈
# 一眼用最小堆来实现啊
# 完全忘记了. 13:13勉强把输入输出写出来了，但是忘记了heapq是直接import，没有from的

# @lc code=start
# import heapq
# class MinStack:

#     def __init__(self):
#         self.st = []

#     def push(self, val: int) -> None:
#         self.st.heapqpush(val)

#     def pop(self) -> None:
#         self.st.heapqpop()

#     def top(self) -> int:
#         return self.st[-1]

#     def getMin(self) -> int:
#         return self.st[0]       
from math import inf 
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

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
import sys
data = sys.stdin.readlines()
options = data[0].strip().split()
nums = list(map(int, data[1].strip().split()))
end = 0
minstack = None
for op in options:
    if op == "MinStack":
        minstack = MinStack()
    elif op == "push":
        minstack.push(nums[end])
        end+=1
    elif op == "pop":
        minstack.pop()
    elif op == "getMin":
        print(minstack.getMin())
    else:
        print(minstack.top())


#
# @lcpr case=start
# ["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]\n
# @lcpr case=end

#


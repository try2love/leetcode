#
# @lc app=leetcode.cn id=901 lang=python3
# @lcpr version=30400
#
# [901] 股票价格跨度
#
from math import inf
# @lc code=start
class StockSpanner:
    # 维护一个递减的单调栈
    def __init__(self):
        self.st = []
    def next(self, price:int):
        ans = 1
        while self.st and self.st[-1][0]<=price:
            ans += self.st.pop()[1]
        self.st.append((price,ans))
        return ans

    # def __init__(self):
    #     self.st = [(-1, inf)]
    #     self.cur_day = -1

    # def next(self, price: int) -> int:
    #     while price>=self.st[-1][1]:
    #         self.st.pop()
    #     self.cur_day += 1
    #     ans = self.cur_day - self.st[-1][0]
    #     self.st.append((self.cur_day,price))
    #     return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

import sys
def solve():
    op = sys.stdin.readline().strip().split()
    if len(op)<=1:
        return
    op = op[1:]
    prices = list(map(int, sys.stdin.readline().strip().split()))
    s = StockSpanner()
    for price in prices:
        print(s.next(price))

solve()
#
# @lcpr case=start
# ["StockSpanner","next","next","next","next","next","next","next"]\n[[],[100],[80],[60],[70],[60],[75],[85]]\n
# @lcpr case=end

#


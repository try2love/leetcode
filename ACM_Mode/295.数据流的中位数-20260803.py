#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30404
#
# [295] 数据流的中位数
# 完全没有印象，直接看答案
from heapq import heappushpop, heappush
# @lc code=start
class MedianFinder:
    def __init__(self):
        self.left= [] # 最大堆
        self.right = [] # 最小堆

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heappush(self.left, -heappushpop(self.right, num))
        else:
            heappush(self.right, -heappushpop(self.left, -num))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end



#
# @lcpr case=start
# ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]\n
# @lcpr case=end

#


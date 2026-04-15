#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30403
#
# [295] 数据流的中位数
#
import heapq
# @lc code=start
# -----参考答案------
class MedianFinder:
    def __init__(self):
        self.left = [] # 最大堆
        self.right = [] # 最小堆
    def addNum(self, num:int) -> None:
        if len(self.left) == len(self.right):
            heapq.heappush_max(self.left, heapq.heappushpop(self.right, num))
        else:
            heapq.heappush(self.right, heapq.heappushpop_max(self.left, num))
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0]
        return (self.left[0] + self.right[0]) / 2
    
# 正统写法（没有heappushpop_max）
class MedianFinder:
    def __init__(self):
        self.left = [] # 大根堆
        self.right = [] # 小根堆
        # 左max 《= 右min

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heapq.heappush(self.left, -heapq.heappushpop(self.right, num))
        else:
            heapq.heappush(self.right, -heapq.heappushpop(self.left, -num))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (self.right[0] - self.left[0])/2

# -----参考答案------

# class MedianFinder:
#     def __init__(self):
#         self.isodd = False # 表征是不是基数
#         self.q = []
#         heapq.heapify(self.q)

#     def addNum(self, num: int) -> None:
#         self.isodd = False if self.isodd else True
#         heapq.heappush(self.q, num)

#     def findMedian(self) -> float:
#         if self.isodd:
#             return float(self.q[len(self.q)//2])
#         else:
#             return (self.q[len(self.q)//2] + self.q[len(self.q)//2-1])/2


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


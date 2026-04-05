#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30402
#
# [4] 寻找两个正序数组的中位数
# 17:05 不会做，看答案
from typing import List
from math import inf
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n  = len(nums1), len(nums2)
        # 想象维护一个长为m+n // 2的绳子
        if m < n:
            m, n = n, m
            nums1, nums2 = nums2, nums1
        
# -----参考答案------
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a  # 保证下面的 i 可以从 0 开始枚举

        m, n = len(a), len(b)
        a = [-inf] + a + [inf]
        b = [-inf] + b + [inf]

        # 枚举 nums1 有 i 个数在第一组
        # 那么 nums2 有 j = (m + n + 1) // 2 - i 个数在第一组
        i, j = 0, (m + n + 1) // 2
        while True:
            if a[i] <= b[j + 1] and a[i + 1] > b[j]:  # 写 >= 也可以
                max1 = max(a[i], b[j])  # 第一组的最大值
                min2 = min(a[i + 1], b[j + 1])  # 第二组的最小值
                return max1 if (m + n) % 2 else (max1 + min2) / 2
            i += 1  # 继续枚举
            j -= 1

class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a  # 保证下面的 i 可以从 0 开始枚举

        m, n = len(a), len(b)
        a = [-inf] + a + [inf]
        b = [-inf] + b + [inf]

        # 枚举 nums1 有 i 个数在第一组
        # 那么 nums2 有 j = (m + n + 1) // 2 - i 个数在第一组
        i, j = 0, (m + n + 1) // 2
        while a[i + 1] <= b[j]:
            i += 1  # 继续枚举
            j -= 1

        max1 = max(a[i], b[j])  # 第一组的最大值
        min2 = min(a[i + 1], b[j + 1])  # 第二组的最小值
        return max1 if (m + n) % 2 else (max1 + min2) / 2

class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a

        m, n = len(a), len(b)
        # 循环不变量：a[left] <= b[j+1]
        # 循环不变量：a[right] > b[j+1]
        left, right = -1, m
        while left + 1 < right:  # 开区间 (left, right) 不为空
            i = (left + right) // 2
            j = (m + n - 3) // 2 - i
            if a[i] <= b[j + 1]:
                left = i  # 缩小二分区间为 (i, right)
            else:
                right = i  # 缩小二分区间为 (left, i)

        # 此时 left 等于 right-1
        # a[left] <= b[j+1] 且 a[right] > b[(j-1)+1] = b[j]，所以答案是 i=left
        i = left
        j = (m + n - 3) // 2 - i
        ai = a[i] if i >= 0 else -inf
        bj = b[j] if j >= 0 else -inf
        ai1 = a[i + 1] if i + 1 < m else inf
        bj1 = b[j + 1] if j + 1 < n else inf
        max1 = max(ai, bj)
        min2 = min(ai1, bj1)
        return max1 if (m + n) % 2 else (max1 + min2) / 2

# @lc code=end
import sys
import json
nums1 = json.loads(sys.stdin.readline().strip())
nums2 = json.loads(sys.stdin.readline().strip())
sol = Solution()


#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#


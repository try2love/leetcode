#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30404
#
# [4] 寻找两个正序数组的中位数
# 3:49 直接看答案
from typing import List
from math import inf
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        # 参考
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
    
        m, n = len(nums1), len(nums2)
        target = (m+n)//2
        if m>n:
            m,n,nums1,nums2 = n,m,nums2,nums1
        # nums1较短
        l1, r1 = 0, m

        
# @lc code=end



#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#


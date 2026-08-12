#
# @lc app=leetcode.cn id=4 lang=python3
# @lcpr version=30404
#
# [4] 寻找两个正序数组的中位数
# 9:50还是不能流畅写出来
from typing import List
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # if len(nums1) < len(nums2):
        #     nums1, nums2 = nums2, nums1
        # m, n = len(nums1), len(nums2)
        # 参考
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo+hi)//2
            j = (m+n+1)//2-i
            left1 = nums1[i-1] if i>0 else float('-inf')
            right1 = nums1[i] if i<m else float('inf')
            left2 = nums2[j-1] if j>0 else float('-inf')
            right2 = nums2[j] if j<n else float('inf')
            if left1 <= right2 and left2 <= right1:
                if (m+n)%2==1:
                    return max(left1, left2)
                return (max(left1, left2)+min(right1, right2))/2
            elif left1 > right2:
                hi = i-1
            else:
                lo = i+1

        # target = (m+n)//2
        # a,b,c,d = target-1, target, -1, 0
        # left = 0
        # right = m
        # while left < right:
        #     if nums1[a]<nums2[d] and nums2[c] < nums1[b]:
        #         break

        # if (m+n)%2 == 0:
        #     return (nums1[b]+nums2[d])
        
# @lc code=end



#
# @lcpr case=start
# [1,3]\n[2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#


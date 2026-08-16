#
# @lc app=leetcode.cn id=88 lang=python3
# @lcpr version=30404
#
# [88] 合并两个有序数组
# 14:55 没做出来
from typing import List
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 参考答案
        p1, p2, p = m-1, n-1, m+n-1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        return

        # 应该是双指针
        left = m-1
        right = n-1
        end = m+n-1
        buttom = m-1
        while end >= buttom and right>=0 and left>=0:
            if nums1[left] <= nums2[right]:
                nums1[end],nums2[right] = nums2[right],nums1[end]
                right -= 1
            else:
                nums1[end],nums1[left] = nums1[left],nums1[end]
                left -= 1
                buttom -= 1
            end -= 1
        return

        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,0,0,0]\n3\n[2,5,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n[]\n0\n
# @lcpr case=end

# @lcpr case=start
# [0]\n0\n[1]\n1\n
# @lcpr case=end

#


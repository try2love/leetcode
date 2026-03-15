#
# @lc app=leetcode.cn id=35 lang=python3
# @lcpr version=30400
#
# [35] 搜索插入位置
# 6:37 ACM AC，实际上几秒钟就写好了核心，因为有bisect_left
from typing import List
from bisect import bisect_left
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # return bisect_left(nums, target)
        # 手写二分查找
        left, right = 0, len(nums) # 左闭右开
        while left < right:
            middle = left + (right - left)//2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1
        return left
# @lc code=end

import sys
data = sys.stdin.readline().strip().split()
data = [int(x) for x in data]
target = eval(input())
sol = Solution()
print(sol.searchInsert(data, target))


#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#


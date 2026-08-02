#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30404
#
# [215] 数组中的第K个最大元素
# 8:06 没做出来
from typing import List
import heapq
from random import randint
# @lc code=start
class Solution:
    def paratition(self, nums:List[int], left:int, right:int) -> int:
        i = randint(left, right)
        pivot = nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        i, j = left+1, right
        while True:
            while i<=j and nums[i] < pivot:
                i += 1
            while i<=j and nums[j] > pivot:
                j -= 1
            if i>=j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        nums[left], nums[j] = nums[j], nums[left]
        return j
    
    def findKthLargest(self, nums: List[int], k:int) -> int:
        n = len(nums)
        target_idx = n-k
        left, right = 0, n-1
        while True:
            i = self.paratition(nums, left, right)
            if i == target_idx:
                return nums[i]
            if i>target_idx:
                right = i-1
            else:
                left = i+1
# -----参考答案------
        # 快速选择参考答案
        n = len(nums)
        target_index = n-k
        left, right = 0, n-1
        while True:
            i = self.partition(nums, left, right)
            if i == target_index:
                return nums[i]
            if i > target_index:
                right = i-1
            else:
                left = i+1
            

        # 堆排序参考答案
        target = [x for x in nums[:k]]
        heapq.heapify(target)
        for i in range(k, len(nums)):
            heapq.heappushpop(target, nums[i])
        return target[0]

        # 一下子想到的是堆排序，小顶堆
        # 如果是单调栈呢
        nums = [-x for x in nums]
        print(nums)
        h = nums[:k]
        heapq.heapify(h)
        for x in nums[k:]:
            if x >= h[-1]:
                heapq.heappop(h)
                heapq.heappush(h, x)
        print(h)
        return -h[-1]

# @lc code=end



#
# @lcpr case=start
# [3,2,1,5,6,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,1,2,4,5,5,6]\n4\n
# @lcpr case=end

#


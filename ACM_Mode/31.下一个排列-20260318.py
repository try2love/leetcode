#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30400
#
# [31] 下一个排列
# 耗时28:30，没有a出来
from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 查阅答案之后的做法：首先找出来x，x具有这样的特征：它比右边的数字小
        # 接下来从x后面倒着找第一个大于x的数字，交换x和y，现在y是高位，然后反转y后面的数字
        # 因为交换后，y后面的数字还是单调不增的
        n = len(nums)
        i = n-2
        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i>=0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return

        
        # 本质上是从后往前找第一个递减的序列，如果整体都递减，那么直接反转
        right = len(nums) - 1
        left = right
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= nums[left]:
                left -= 1
            else:
                break
        if left == 0:
            # 问题1: 最开始没有[:]赋值
            nums[:] = nums[::-1]
        else:
            # 问题2: 输入132，期望输出213，输出了312
            # nums[left-1], nums[left] = nums[left], nums[left-1]
            # nums = nums[:left] + sorted(nums[left:])
            # 需要找递减有序的最小大于left-1的书
            tmp = nums[left-1]
            target = right
            for idx,x in enumerate(nums[left::-1]):
                if x > tmp:
                    target = idx
                    break
            nums[left-1], nums[target] = nums[target], nums[left-1]
            nums[:] = nums[:left] + sorted(nums[left:])

        return
# @lc code=end
import sys
data = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
sol.nextPermutation(data)
print(data)

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#


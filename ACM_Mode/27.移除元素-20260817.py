#
# @lc app=leetcode.cn id=27 lang=python3
# @lcpr version=30404
#
# [27] 移除元素
# 5:37 ACM AC
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 参考答案：栈
        stack_size = 0
        for x in nums:
            if x != val:
                nums[stack_size] = x
                stack_size += 1
        return stack_size

        # 双指针，遇到val就替换
        n = len(nums)
        left = 0
        right = n-1
        while left <= right:
            while right >= 0:
                if nums[right] == val:
                    right -= 1
                else:
                    break
            while left < n:
                if nums[left] != val:
                    left += 1
                else:
                    break
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return left
# @lc code=end



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#


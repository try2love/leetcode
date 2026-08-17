#
# @lc app=leetcode.cn id=80 lang=python3
# @lcpr version=30404
#
# [80] 删除有序数组中的重复项 II
# 4:15 ACM AC
from collections import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 参考答案
        stack_size = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[stack_size-2]:
                nums[stack_size] = nums[i]
                stack_size += 1
        return min(stack_size, len(nums))

        stack_size = 0
        cnt = 1
        for x in nums[1:]:
            if x == nums[stack_size]:
                if cnt < 2:
                    cnt += 1
                    stack_size += 1
                    nums[stack_size] = x
                else:
                    continue
            elif x != nums[stack_size]:
                cnt = 1
                stack_size += 1
                nums[stack_size] = x
        return stack_size+1
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,1,2,3,3]\n
# @lcpr case=end

#


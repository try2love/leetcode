#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30404
#
# [26] 删除有序数组中的重复项
# 2:50 ACM AC
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack_size = 0
        for x in nums[1:]:
            if x == nums[stack_size]:
                continue
            else:
                stack_size += 1
                nums[stack_size] = x
        return stack_size + 1
        
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#


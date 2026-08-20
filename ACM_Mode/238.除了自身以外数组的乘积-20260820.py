#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30404
#
# [238] 除了自身以外数组的乘积
# 6:03 ACM AC
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 前缀积和后缀积
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i, x in enumerate(nums):
            if i == 0:
                continue
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        # print(prefix)
        # print(suffix)
        for idx, suf in enumerate(suffix):
            prefix[idx] *= suf
        return prefix
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30404
#
# [53] 最大子数组和
# 8:43 ACM AC
from typing import List
from collections import defaultdict
from math import inf
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i-1], 0) + nums[i]
        return max(f)
        
        # 前缀和 + 贪心
        ans = -inf
        min_pre_sum = pre_sum = 0
        for x in nums:
            pre_sum += x
            ans = max(ans, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        return ans
        
        # 前缀和
        if len(nums) == 0:
            return 0
        ans = nums[0]
        pre_sum = [0] * (len(nums) + 1)
        left_min = 0
        for idx,x in enumerate(nums):
            pre_sum[idx+1] = pre_sum[idx] + x
            ans = max(ans, pre_sum[idx+1] - left_min)
            if pre_sum[idx+1] < left_min:
                left_min = pre_sum[idx+1]
        return ans

# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.maxSubArray(nums))

#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#


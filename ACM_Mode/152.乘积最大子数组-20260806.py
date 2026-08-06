#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30404
#
# [152] 乘积最大子数组
# 7:30 没有思路，直接看答案
from typing import List
from math import inf
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 三种状态：
        # 选择第i个加入；选择第i个从头开始；不选第i个
        # 不对，这不是前缀积吗，但是有0存在
        # pre = [1]*(len(nums)+1)
        # for i,x in enumerate(nums):
        #     pre[i+1] = pre[i]*x
        ans = -inf
        f_max = f_min = 1
        for x in nums:
            if x<0:
                f_max, f_min = f_min, f_max
            f_max = max(f_max * x, x)
            f_min = min(f_min * x, x)
            ans = max(ans, f_max)
        return ans
        
        ans = -inf
        f_max = f_min = 1
        for x in nums:
            f_max, f_min = max(f_max*x, f_min*x, x), min(f_max*x, f_min*x, x)
            ans = max(ans, f_max)
        return ans
        
        n = len(nums)
        f_max = [0]*n
        f_min = [0]*n
        f_max[0] = f_min[0] = nums[0]
        for i in range(1, n):
            x = nums[i]
            f_max[i] = max(f_max[i-1]*x, f_min[i-1]*x, x)
            f_min[i] = min(f_max[i-1]*x, f_min[i-1]*x, x)
        return max(f_max)

# @lc code=end



#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#


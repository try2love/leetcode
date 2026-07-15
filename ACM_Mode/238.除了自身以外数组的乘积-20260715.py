#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30404
#
# [238] 除了自身以外数组的乘积
# 7min没有思路，直接看答案
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 减少空间
        n = len(nums)
        suf = [1] * n
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        pre = 1
        for i,x in enumerate(nums):
            suf[i] *= pre
            pre *= x
        return suf
        
        # 参考答案
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        suf = [1] * n
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        return [p*s for p,s in zip(pre, suf)]


        # 看了参考答案后尝试写出来：
        left_mul = [1] * (len(nums)+1)
        right_mul = [1] * (len(nums)+1)
        for idx,n in enumerate(nums):
            left_mul[idx+1] = left_mul[idx] * n
        for idx,n in enumerate(nums[::-1]):
            right_mul[idx+1] = right_mul[idx] * n
        print(left_mul)
        print(right_mul[::-1])
        right_mul = right_mul[::-1]
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = left_mul[i] * right_mul[i+1]
        return ans


# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.productExceptSelf(nums))


#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#


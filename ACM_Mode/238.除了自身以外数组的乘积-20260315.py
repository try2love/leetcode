#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30400
#
# [238] 除了自身以外数组的乘积
# 不让用除法，还要求on，一下子真让我没了思路，那前缀积和后缀集
# 8:52 实现了钱后缀积的做法，但是空间复杂度为o(2n)，能不能优化空间？
# 14:24实现了空间的优化，只用了一个额外的ans数组。
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 既然输出数组不算，那么久用一个tmp来维护前缀或者后缀
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        nxt = 1
        for j in range(len(nums)-2, -1, -1):
            nxt *= nums[j+1]
            ans[j] *= nxt
        return ans
        # pre = [1]*len(nums)
        # nxt = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     pre[i] = pre[i-1] * nums[i-1]
        # for j in range(len(nums)-2, -1, -1):
        #     nxt[j] = nxt[j+1] * nums[j+1]
        # for i in range(len(nums)):
        #     nums[i] = pre[i] * nxt[i]
        # return nums
# @lc code=end

import sys
data = sys.stdin.readline().strip().split()
data = [int(x) for x in data]
sol = Solution()
print(sol.productExceptSelf(data))

#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#


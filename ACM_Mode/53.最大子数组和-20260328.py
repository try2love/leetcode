#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30401
#
# [53] 最大子数组和
# 24:20 没有做出来，[-2,-1]输出了0而不是期望的-1
from typing import List
from math import inf
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # -----参考答案------
        ans = -inf
        min_pre_sum = pre_sum = 0
        for x in nums:
            pre_sum += x
            ans = max(ans, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        return ans
    
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i-1], 0) + nums[i]
        return max(f)
    
        ans = -inf
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans
        # -----参考答案------

        # 前缀和
        if len(nums) == 1:
            return nums[0]
        prefix = [0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        # 一次遍历，维护min和max，行不通，有方向问题
        ans = -inf
        min_pre = max_pre = prefix[0]
        for i in range(len(prefix)):
            x = prefix[i]
            if x < min_pre:
                min_pre = max_pre = x
                ans = max(ans, x)
            else:
                max_pre = max(max_pre, x)
                ans = max(ans, max_pre-min_pre)
        # 单调栈，维护一个递增单调栈 单调栈行不通
        # st = [(-1,inf)]
        # for i in range(1, len(prefix)):
        #     while len(st)>1 and st[-1][1] > prefix[i]:
        #         if len(st) == 2:
        #             ans = max(ans, st.pop()[1] - st[1][1])
        #         else:
        #             ans = max(ans, st.pop()[1])
        #     st.append((i, prefix[i]))
        return ans

# @lc code=end

import sys
nums = list(map(int, sys.stdin.readline().strip().split()))
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


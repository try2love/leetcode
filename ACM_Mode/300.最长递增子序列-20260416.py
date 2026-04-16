#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30403
#
# [300] 最长递增子序列
# 10min没有思路，完全忘记怎么写了
from typing import List
from functools import cache
from bisect import bisect_left
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # -----参考答案------
        ng = 0
        for x in nums:
            j = bisect_left(nums, x, 0, ng)
            nums[j] = x
            if j == ng:
                ng += 1
        return ng

        g = []
        for x in nums:
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
        return len(g)

        dp = [0] * len(nums)
        for i,x in enumerate(nums):
            for j,y in enumerate(nums[:i]):
                if x > y:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp)

        @cache
        def dfs(i:int):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1
        return max(dfs(i) for i in range(len(nums)))
        # -----参考答案------

        # 单调递增栈？回溯？？
        def dfs(i:int):
            if i<0:
                return 0
            return max(dfs(i-1)+1)

# @lc code=end



#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#


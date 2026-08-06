#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30404
#
# [300] 最长递增子序列
# 5：20 没有思路
from typing import List
from functools import cache
from math import inf
from bisect import bisect_left
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 参考
        ng = 0
        for x in nums:
            j = bisect_left(nums, x, 0, ng)
            nums[j] = x
            if j == ng:
                ng += 1
        return ng

        g = []
        for x in nums:
            j = bisect_left(g,x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
        return len(g)

        f = [0] * len(nums)
        for i,x in enumerate(nums):
            for j,y in enumerate(nums[:i]):
                if x>y:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        return max(f)

        @cache
        def dfs(i:int) -> int:
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res+1
        return max(dfs(i) for i in range(len(nums)))
        # 每一个元素都有选或不选两种情况
        # @cache
        # def dfs(i:int, pre:int):

        
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


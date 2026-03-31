#
# @lc app=leetcode.cn id=213 lang=python3
# @lcpr version=30402
#
# [213] 打家劫舍 II
# 腾讯一面手撕题，到现在我还是没好思路
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def rob1(self, nums:List[int]) -> int:
        f0 = f1 = 0
        for x in nums:
            f0, f1 = f1, max(f0+x, f1)
        return f1

    def rob(self, nums: List[int]) -> int:
        # -----参考答案------
        n = len(nums)
        @cache
        def dfs(i:int, bound:int):
            if i < bound:
                return 0
            return max(nums[i]+dfs(i-2, bound), dfs(i-1, bound))
        return max(nums[-1]+dfs(n-3, 1), dfs(n-2, 0))

        return max(nums[0] + self.rob1(nums[2:-1]), self.rob1(nums[1:]))
        # -----参考答案------

        n = len(nums)
        @cache
        def dfs(i:int):
            if i < 0:
                return 0
            return max(dfs(i-1), dfs(i-2)+nums[i])
        return dfs(n-1)

# @lc code=end
import sys
data = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.rob(data))


#
# @lcpr case=start
# [2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#


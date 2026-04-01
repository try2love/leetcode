#
# @lc app=leetcode.cn id=213 lang=python3
# @lcpr version=30402
#
# [213] 打家劫舍 II
# 4:45 ACM AC
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def rob1(self, nums:List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i:int):
            if i < 0:
                return 0
            return max(dfs(i-1), dfs(i-2) + nums[i])
        return dfs(n-1)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
        

# @lc code=end
import sys
# 需要考虑null的问题
nums = sys.stdin.readline()
if nums == "null":
    print(0)
else:
    nums = list(map(int, nums.strip().split()))
    sol = Solution()
    print(sol.rob(nums))


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


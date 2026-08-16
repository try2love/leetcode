#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30404
#
# [279] 完全平方数
# 8:34 ACM AC
from functools import cache
import math
# @lc code=start
nums = [x**2 for x in range(1, 101)]
@cache
def dfs(i:int, target:int):
    if i<=0:
        return target
    if target == 0:
        return 0
    if nums[i] > target:
        return dfs(i-1, target)
    return min(dfs(i-1, target), dfs(i, target-nums[i])+1)
class Solution:
    def numSquares(self, n: int) -> int:
        # print(nums)
        return dfs(math.isqrt(n)-1, n)
# @lc code=end
n = eval(input())
sol = Solution()
print(sol.numSquares(n))


#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#


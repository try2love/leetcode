#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30403
#
# [70] 爬楼梯
# 3:22 ACM AC 用了记忆化搜索
from functools import cache
# @lc code=start
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0] * (n+1)
        f[0] = f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]
    
        f0 = f1 = 1
        for _ in range(2, n+1):
            f0, f1 = f1, f1+f0
        return f1

# @lc code=end

n = eval(input())
sol = Solution()
print(sol.climbStairs(n))


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#


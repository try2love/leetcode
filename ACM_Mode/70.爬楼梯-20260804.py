#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30404
#
# [70] 爬楼梯
# 5:16 ACM AC
from functools import cache
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 参考
        f0 = f1 = 1
        for _ in range(2, n+1):
            f0, f1 = f1, f1+f0
        return f1

        f = [0] * (n+1)
        f[0] = f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

        @cache
        def dfs(i:int) -> int:
            if i<=1:
                return 1
            return dfs(i-1) + dfs(i-2)
        return dfs(n)

        
        @cache
        def dfs(i:int):
            if i<=0:
                return 0
            elif i==1:
                return 1
            elif i==2:
                return 2
            return dfs(i-1) + dfs(i-2)
        return dfs(n)
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#


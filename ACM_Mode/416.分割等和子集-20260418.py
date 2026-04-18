#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30403
#
# [416] 分割等和子集
# 5:36 记忆化搜索 8:59 二维动态规划，但是感觉写的很别扭
from typing import List
from functools import cache
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # -----参考答案------
        s = sum(nums)
        if s%2:
            return False
        s //= 2

        f = 1
        for x in nums:
            f |= f << x
        return (f >> s & 1) == 1

        n = len(nums)
        dp = [True] + [False] * s
        s2 = 0
        for i,x in enumerate(nums):
            s2 = min(s2+x, s)
            for j in range(s2, x-1, -1):
                dp[j] = dp[j] or dp[j-x]
            if dp[s]:
                return True
        return False

        dp = [[False]*(s+1) for _ in range(n+1)]
        dp[0][0] = True
        for i,x in enumerate(nums):
            for j in range(s+1):
                dp[i+1][j] = j>=x and dp[i][j-x] or dp[i][j]
        return dp[n][s]

        @cache
        def dfs(i:int, j:int):
            if i<0:
                return j==0
            return j>=nums[i] and dfs(i-1,j-nums[i]) or dfs(i-1, j)
        s = sum(nums)
        return s%2==0 and dfs(len(nums)-1, s//2)

        @cache
        def dfs(i:int, j:int):
            if i<0:
                return j==0
            if j<nums[i]:
                return dfs(i-1,j)
            return dfs(i-1, j-nums[i]) or dfs(i-1, j)
        s = sum(nums)
        return s%2==0 and dfs(len(nums)-1, s//2)
    
        # 我自己之前写的版本
        total = sum(nums)
        if total % 2 == 1:
            return False
        total = total // 2
        n = len(nums)
        dp = [True] + [False]*total
        for i,x in enumerate(nums):
            for j in range(total, -1, -1):
                if j >= x:
                    dp[j] = dp[j] or dp[j-x]
        return dp[-1]

        dp = [[False] * (total+1) for _ in range(2)]
        for i in range(2):
            dp[i][0] = True
        for i in range(n):
            for j in range(total+1):
                if j < nums[i]:
                    dp[(i+1)%2][j] = dp[i%2][j]
                else:
                    dp[(i+1)%2][j] = dp[i%2][j] or dp[i%2][j-nums[i]]
        return dp[n%2][total]

        @cache
        def dfs(i:int, target:int):
            if i < 0 or target < 0: # 因为nums是正数，所以可以对target判断
                return False
            if target == 0:
                return True
            return dfs(i-1, target) or dfs(i-1, target - nums[i])
        return dfs(n-1, total)

        # -----参考答案------

        total = sum(nums)
        if total % 2 == 1:
            return False
        nums.sort()
        target = total // 2
        dp = [[False] * (total+1) for _ in range(len(nums)+1)]
        # dp[target] = [True] * (len(nums)+1)
        for i in range(len(nums)):
            dp[i][0] = True
            for j in range(total):
                if j>=nums[i]:
                    dp[i+1][j] = dp[i][j] or dp[i][j-nums[i]]
                else:
                    dp[i+1][j] = dp[i][j]
        return dp[-1][target]
    
        @cache
        def dfs(i:int, cur:int):
            if i<0:
                return cur==0
            if cur == 0:
                return True
            return dfs(i-1, cur) or dfs(i-1, cur-nums[i])
        return dfs(len(nums)-1, target)    

        @cache
        def dfs(i:int, cur:int):
            if i<0:
                return cur==target
            if cur == target:
                return True
            return dfs(i-1, cur) or dfs(i-1, cur+nums[i])
        return dfs(len(nums)-1, 0)


# @lc code=end



#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=3840 lang=python3
# @lcpr version=30402
#
# [3840] 打家劫舍 V
# 12:55 没有做出来，看答案
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        # -----参考答案------
        n = len(nums)
        f = [0] * (n+1)
        f[1] = nums[0]
        for i in range(1, n):
            if colors[i] != colors[i-1]:
                f[i+1] = f[i] + nums[i]
            else:
                f[i+1] = max(f[i-1]+nums[i], f[i])
        return f[n]
    
        # 空间优化;
        f0, f1 = 0, nums[0]
        for i in range(1, len(nums)):
            if colors[i] != colors[i-1]:
                f0 = f1
                f1 += nums[i]
            else:
                f0, f1 = f1, max(f0+nums[i], f1)
        return f1
        # -----参考答案------

        def dfs(i:int, col:int): # col记录上一个选择的结果的颜色
            if i<0:
                return 0
            x, c = nums[i], colors[i]
            if c != col:
                return dfs(i-1, c) + x
            if i-1 >= 0:
                return max(dfs(i-1, c)+x, dfs(i-2, c)+x) if c!=colors[i] else max(dfs(i-2, c)+x, dfs(i-1, col))
            else:
                # i==0
                return nums[0] if col != c else 0
        return dfs(len(nums)-1, colors[-1])
# @lc code=end



#
# @lcpr case=start
# [1,4,3,5]\n[1,1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,2,4]\n[2,3,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [10,1,3,9]\n[1,1,1,2]\n
# @lcpr case=end

#


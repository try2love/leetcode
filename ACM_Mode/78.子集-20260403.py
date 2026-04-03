#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30402
#
# [78] 子集
# 3:30 ACM AC
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # -----参考答案------
        # 答案视角的枚举选哪个
        n = len(nums)
        ans = []
        path = []
        def dfs(i:int):
            ans.append(path[:])
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans
        # 二进制枚举
        ans = []
        for i in range(1 << len(nums)):
            subset = [x for j, x in enumerate(nums) if i>>j & 1]
            ans.append(subset)
        return ans
        # -----参考答案------

        # 一眼回溯
        n = len(nums)
        ans = []
        tmp = []
        def dfs(i:int):
            if i>=n:
                ans.append(tmp[:])
                return
            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()
            dfs(i+1)
        dfs(0)
        return ans
# @lc code=end
import sys
nums = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.subsets(nums))

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30400
#
# [46] 全排列
# 9:01 ACM AC，这是一个回溯问题，本质上还是暴力，但是不用写多个for
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 0x3f做法
        n = len(nums)
        path = [0] * n # (路径长度一致)
        on_path = [False] * n
        ans = []

        def dfs(i:int):
            if i==n:
                ans.append(path[:])
                return
            for j,on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i+1)
                    on_path[j] = False
        dfs(0)
        return ans

        # ans = []
        # visited = [0]*len(nums)
        # tmp = []
        # def dfs(i:int):
        #     if len(tmp) == len(nums):
        #         ans.append(tmp[:])
        #         return
        #     # if visited[i] or i>=len(nums):
        #     #     return
        #     for j in range(len(nums)):
        #         if visited[j] == 0:
        #             tmp.append(nums[j])
        #             visited[j] = 1
        #             dfs(j)
        #             tmp.pop()
        #             visited[j] = 0
        #     return
        # dfs(0)
        # return ans

# @lc code=end

import sys
nums = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.permute(nums))


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


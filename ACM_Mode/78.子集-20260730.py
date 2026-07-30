#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30404
#
# [78] 子集
# 5:41
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 参考答案
        n = len(nums)
        ans =  []
        path = []
        def dfs(i:int):
            ans.append(path[:])
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans

        def dfs(i:int) -> None:
            if i==n:
                ans.append(path[:])
                return
            dfs(i+1)
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        dfs(0)
        return ans

        ans = [[]]
        def dfs(i:int, tmp:List[int]):
            # 对于每一个index，都有选或不选两种状态
            if i >= len(nums):
                return
            # 选
            tmp.append(nums[i])
            ans.append(tmp[:])
            dfs(i+1, tmp)
            # 不选
            tmp.pop()
            dfs(i+1, tmp)
        dfs(0, [])
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


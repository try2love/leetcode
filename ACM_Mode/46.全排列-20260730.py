#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30404
#
# [46] 全排列
# 应该是回溯，忘了怎么写，直接看答案
from  typing import List, Set
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n
        ans = []
        def dfs(i:int, remain: Set[int]) -> None:
            if i == n:
                ans.append(path[:])
                return
            for x in remain:
                path[i] = x
                dfs(i+1, remain-{x})
        dfs(0, set(nums))
        return ans

        n = len(nums)
        path = [0] * n
        on_path = [False] * n
        ans = []
        def dfs(i:int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            for j, on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i+1)
                    on_path[j] = False
        dfs(0)
        return ans
     
# @lc code=end



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


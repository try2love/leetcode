#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30401
#
# [39] 组合总和
# 5:00 ACM AC
from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 完全背包问题
        ans = []
        path = []
        def dfs(i:int, target:int):
            if target == 0:
                ans.append(path[:])
                return
            if i < 0:
                return
            if target >= candidates[i]:
                path.append(candidates[i])
                dfs(i, target-candidates[i])
                path.pop()
            dfs(i-1, target)
        dfs(len(candidates)-1, target)
        return ans

# @lc code=end
import sys
candidates = list(map(int, sys.stdin.readline().strip().split()))
target = eval(input())
sol = Solution()
print(sol.combinationSum(candidates, target))


#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#


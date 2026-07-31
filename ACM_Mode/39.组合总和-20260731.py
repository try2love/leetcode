#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30404
#
# [39] 组合总和
# 15:07，结果中还是有重复，如果剪枝，那么结果会少
from typing import List
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 参考答案
        ans = []
        path = []
        def dfs(i:int, left:int) -> None:
            if left == 0:
                ans.append(path[:])
                return
            for j in range(i, len(candidates)):
                if candidates[j] > left:
                    break
                path.append(candidates[j])
                dfs(j, left-candidates[j])
                path.pop()
        dfs(0, target)
        return ans

        def dfs(i:int, left:int) -> None:
            if left == 0:
                ans.append(path[:])
                return
            if i == len(candidates) or left < candidates[i]:
                return
            dfs(i+1, left)
            path.append(candidates[i])
            dfs(i, left-candidates[i])
            path.pop()
        dfs(0, target)
        return ans

        def dfs(i:int, left:int) -> None:
            if left == 0:
                ans.append(path[:])
                return
            if i == len(candidates) or left < 0:
                return
            
            path.append(candidates[i])
            dfs(i, left-candidates[i])
            path.pop()

            dfs(i+1, left)
        dfs(0, target)
        return ans

        candidates.sort()
        ans = []
        path = []
        def dfs(i:int, target:int):
            if target == 0:
                ans.append(path[:])
                return True
            if i>=len(candidates) or target < 0 or target < candidates[i]:
                return False
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                if not dfs(j, target-candidates[j]):
                    path.pop()
                    break
                path.pop()
        for i in range(len(candidates)):
            dfs(i, target)
        # dfs(0, target)
        return ans
# @lc code=end
import sys
import json

can = json.loads(sys.stdin.readline().strip())
target = eval(input())
sol = Solution()
print(sol.combinationSum(can, target))

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


#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30404
#
# [200] 岛屿数量
# 5:21 核心AC，输入写不出来了
from typing import List
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 图的DFS
        ans = 0
        def dfs(i:int, j:int):
            if i<0 or j<0 or i>= len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            return

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == '1':
                    ans += 1
                    dfs(i, j)
        return ans
        
# @lc code=end

import json
import sys
grid = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(grid)
print(sol.numIslands(grid))
# import sys
# data = sys.stdin.readlines()
# grid = []
# for line in data:
#     grid.append(line.strip().split())
# sol = Solution()
# print(grid)
# print(sol.numIslands(grid))

#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30400
#
# [200] 岛屿数量
# 9:00 ACM AC
from typing import List
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        def dfs(i:int, j:int):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!="1":
                return 0
            # 已经确定是1了
            grid[i][j] = "2"
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans
            
# @lc code=end

import sys
data = sys.stdin.readlines()
grid = []
for line in data:
    grid.append(line.strip().split())
sol = Solution()
print(sol.numIslands(grid))


#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#


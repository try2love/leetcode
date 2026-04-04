#
# @lc app=leetcode.cn id=994 lang=python3
# @lcpr version=30402
#
# [994] 腐烂的橘子
# 37:51 ACM AC 但是开销很大，修改了很多版，急需看答案
from typing import List
from collections import deque

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # -----参考答案------
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1 # 新鲜橘子个数
                elif x == 2:
                    q.append((i,j)) # 一开始就腐烂的橘子
        ans = 0
        while q and fresh:
            ans += 1 # 经过一分钟
            tmp = q
            q = []
            for x, y in tmp:
                for i, j in (x-1,y), (x+1,y), (x,y-1), (x,y+1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                        q.append((i,j))
        return -1 if fresh else ans
        # -----参考答案------

        # 先遍历，如果有孤岛，那么直接返回-1
        m, n = len(grid), len(grid[0])
        ans, rotten = self.island(grid)
        if ans==0:
            return 0
        # rotten = deque([])
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 2:
                    rotten.append((i,j))

        def dfs(i:int, j:int):
            if i<0 or i>=m or j<0 or j>=n:
                return
            if grid[i][j] == 1:
                grid[i][j] = 2
                rotten.append((i,j))

        ans = -1
        while rotten:
            ans += 1
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i,j+1)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    return -1
        return ans

    def island(self, grid:List[List[int]]):
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        rotten = deque([])
        def dfs(i:int, j:int):
            if i<0 or i>=m or j<0 or j>=n or visited[i][j]:
                return
            if grid[i][j] == 2:
                rotten.append((i,j))
            visited[i][j] = 1
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if grid[i][j] > 0:
                    ans += 1
                    dfs(i,j)
        return ans, rotten
# @lc code=end
import sys
import json
grid = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.orangesRotting(grid))

#
# @lcpr case=start
# [[2,1,1],[1,1,0],[0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,1],[0,1,1],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2]]\n
# @lcpr case=end

#


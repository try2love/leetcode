#
# @lc app=leetcode.cn id=994 lang=python3
# @lcpr version=30403
#
# [994] 腐烂的橘子
#
from typing import List
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
                    fresh += 1
                elif x == 2:
                    q.append((i,j))
        ans = 0
        while q and fresh:
            ans += 1 # 经过1min
            tmp = q
            q = []
            for x, y in tmp:
                for i,j in (x-1,y), (x+1,y), (x,y-1), (x,y+1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                        q.append((i,j))
        return -1 if fresh else ans
        # -----参考答案------

        # 这个做法是错误的，因为没有考量到同时污染，必须用一个额外的东西维护2腐烂的橘子
        m, n = len(grid), len(grid[0])
        fresh = 0
        ans = 0
        cur_cost = 0
        def dfs(i:int, j:int, time:int):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] not in [1,2]:
                return 0
            nonlocal fresh
            if grid[i][j] == 1:
                grid[i][j] = -1
                fresh -= 1
            for x,y in ((-1,0), (0,-1), (1,0), (0,1)):
                dfs(i+x, j+y, time+1)
            return time+1
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                if x==1:
                    fresh += 1
        for i,row in enumerate(grid):
            for j,x in enumerate(row):
                if x==2:
                    ans = max(ans, dfs(i,j, -1))
        return ans if fresh==0 else -1
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


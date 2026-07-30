#
# @lc app=leetcode.cn id=994 lang=python3
# @lcpr version=30404
#
# [994] 腐烂的橘子
# 16:48 ACM AC
from typing import List
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 参考答案
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1
                elif x == 2:
                    q.append((i, j))
        ans = 0
        while q and fresh:
            ans += 1
            tmp = q
            q = []
            for x, y in tmp:
                for i,j in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
                    if 0<=i<m and 0<=j<n and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2
                        q.append((i,j))
        return -1 if fresh else ans

        rotten = []
        fresh = 0
        times = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1
                if x == 2:
                    rotten.append([i,j])
        def dfs(i:int, j:int):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1:
                return
            nonlocal cur, fresh
            cur.append([i,j])
            grid[i][j] = 2
            fresh -= 1

        cur = []
        while len(rotten) or len(cur):
            for [i, j] in rotten:
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
            if not len(cur):
                break
            rotten = cur[:]
            cur = []
            times += 1
        return times if fresh==0 else -1
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


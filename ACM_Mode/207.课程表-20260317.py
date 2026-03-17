#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30400
#
# [207] 课程表
#
from typing import List

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)

        colors = [0]*numCourses
        def dfs(x:int):
            colors[x] = 1 # x正在访问
            for y in g[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True
            colors[x] = 2
            return False
        for i,c in enumerate(colors):
            if c==0 and dfs(i):
                return False
        return True
        
        # # 并查集
        # grid = [-1 for _ in range(numCourses)]
        # for pair in prerequisites:
        #     font, lat = pair[1], pair[0]
        #     grid[lat] = font
        # for course in range(numCourses):
        #     if grid[course]==-1:
        #         continue
        #     while grid[course] != course:
        #         pre = grid[course]
        #         grid[course] = grid[grid[course]]
        #         if grid[course] == pre or grid[course]== -1:
        #             break
        #     if grid[course] == course:
        #         return False
        # return True

# @lc code=end
import sys
n = eval(input())
data = sys.stdin.readlines()
prerequists = []
for line in data:
    prerequists.append(list(map(int, line.strip().split())))
sol = Solution()
print(sol.canFinish(n, prerequists))


#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30404
#
# [207] 课程表
# 4min没有实现思路，直接看答案
from typing import List
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 本质上是有没有成环
        # 参考答案
        g = [[] for _ in range(numCourses)] # 
        for a, b in prerequisites:
            g[b].append(a)
        colors = [0] * numCourses
        def dfs(x:int) -> bool:
            colors[x] = 1 # x访问中
            for y in g[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True
            colors[x] = 2 # x完全访问完毕，从x出发没有环
            return False
        for i,c in enumerate(colors):
            if c == 0 and dfs(i):
                return False
        return True
        
# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#


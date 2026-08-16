#
# @lc app=leetcode.cn id=207 lang=python3
# @lcpr version=30404
#
# [207] 课程表
# 8:10，不管是设置pre还是next，都会有问题，看答案
from typing import List
# @lc code=start
class Node:
    def __init__(self, x=0, pre=None):
        self.val = x
        self.pre = pre

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 参考答案
        g = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            g[b].append(a)
        colors = [0] * numCourses
        def dfs(x:int) -> bool:
            colors[x] = 1
            for y in g[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True
            colors[x] = 2
            return False
        for i,c in enumerate(colors):
            if c == 0 and dfs(i):
                return False
        return True

        courses = [Node(x) for x in range(numCourses)]
        for it in prerequisites:
            b, a = it
            courses[b].pre = courses[a]
        # 判断是否有环
        for course in courses:
            slow = fast = course
            while fast.pre and fast.pre.pre:
                slow = slow.pre
                fast = fast.pre.pre
                if slow==fast:
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


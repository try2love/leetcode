#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30404
#
# [51] N 皇后
# 7:32直接看答案
from typing import List
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 思路：遍历一行，逐个尝试放置皇后，遗忘写法，直接看答案
        ans = []
        # 参考答案
        queens = [0] * n
        col = [False] * n
        diag1 = [False] *(n*2-1)
        diag2 = [False] *(n*2-1)
        def dfs(r:int) -> None:
            if r == n:
                ans.append(['.'*c + 'Q' + '.'*(n-1-c) for c in queens])
                return
            for c, ok in enumerate(col):
                if not ok and not diag1[r+c] and not diag2[r-c]:
                    queens[r] = c
                    col[c] = diag1[r+c] = diag2[r-c] = True
                    dfs(r+1)
                    col[c] = diag1[r+c] = diag2[r-c] = False
        dfs(0)
        return ans

        path = ["."*n for _ in range(n)]
        def dfs(row:int, col:int, cnt:int):
            if cnt == n:
                ans.append(path[:])
                return
            return
        for i in range(n):
            dfs(0,i,1)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30400
#
# [51] N 皇后
# 34分钟做完，包括输入输出测试。
# 整体卡壳的地方：
# 1. 最开始递归思路找错了，还想着应该dfs(i,[]) for i in range(n)，实际上定义的i就是行数，只用dfs(0,[])即可
# 2. 答案写入ans的位置错了，我实在循环里面判断的，所以对于n=1，返回的是空，然后去边界条件添加ans，又出现重复输出的问题，所以答案对于递归回溯问题始终都在边界条件执行
# 3. 早停了，导致n=5答案错误，因为第一行的Q对应有多个答案，如果早停就会把后面正确答案剪枝，所以这个题本身时间还是o(n^2)
from typing import List
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        ans = []
        # 回溯
        def dfs(i:int, pos):
            nonlocal ans
            if i>=n:
                if len(pos) == n:
                    ans.append(["".join(row) for row in board])
                return
            for j in range(n):
                if len(pos) > 0:
                    if any(abs(pair[0]-i)==abs(pair[1]-j) or (pair[0]==i or pair[1]==j) for pair in pos):
                        continue
                    else:
                        pos.append([i,j])
                        board[i][j] = "Q"
                        flag = dfs(i+1, pos)
                        # if flag and len(pos)==n:
                        #     ans.append(["".join(row) for row in board])
                        board[i][j] = "."
                        pos.pop()
                        # return flag
                else:
                    pos.append([i,j])
                    board[i][j] = "Q"
                    dfs(i+1,pos)
                    board[i][j] = "."
                    pos.pop()
            # return False
        dfs(0,[])
        return ans
            
# @lc code=end

import sys
n = sys.stdin.read().strip().split()
n = int(n[0])
solution = Solution()
ans = solution.solveNQueens(n)
print(ans)
#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end
#


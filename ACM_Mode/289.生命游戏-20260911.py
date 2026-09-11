#
# @lc app=leetcode.cn id=289 lang=python3
# @lcpr version=30404
#
# [289] 生命游戏
# 12:42 ACMAC
from typing import List
from copy import deepcopy
# @lc code=start
directions = ((-1,-1), (-1,0), (-1,1),
              (0,-1), (0,1),
              (1,-1), (1,0), (1,1))
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 参考答案
        import numpy as np
        r,c = len(board), len(board[0])
        # zero_padding
        board_exp = np.array([[0 for _ in range(c+2)] for _ in range(r+2)])
        board_exp[1:1+r, 1:1+c] = np.array(board)
        kernal = np.array([[1,1,1], [1,0,1], [1,1,1]])
        for i in range(1, r+1):
            for j in range(1, c+1):
                temp_sum = np.sum(kernal * board_exp[i-1:i+2, j-1:j+2])
                if board_exp[i,j] == 1:
                    if temp_sum < 2 or temp_sum > 3:
                        board[i-1][j-1] = 0
                else:
                    if temp_sum == 3:
                        board[i-1][j-1] = 1
        return

        # 原地修改，一个状态机
        m, n = len(board), len(board[0])
        status = [[0] * n for _ in range(m)]
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                for d in directions:
                    pre_x, pre_y = i+d[0], j+d[1]
                    if 0<=pre_x<m and 0<=pre_y<n:
                        status[i][j] += 1 if board[pre_x][pre_y] else 0
        for i,row in enumerate(status):
            for j,x in enumerate(row):
                if x < 2:
                    board[i][j] = 0
                elif x > 3:
                    board[i][j] = 0
                elif x == 3 and board[i][j] == 0:
                    board[i][j] = 1
        return

# @lc code=end



#
# @lcpr case=start
# [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,0]]\n
# @lcpr case=end

#


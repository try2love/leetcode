#
# @lc app=leetcode.cn id=36 lang=python3
# @lcpr version=30404
#
# [36] 有效的数独
# 8:20放弃思考，关键是怎么表征一个个小正方形中的数字
from typing import List
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 参考答案
        row_has = [[False] * 9 for _ in range(9)]
        col_has = [[False] * 9 for _ in range(9)]
        sub_box_has = [[[False]*9 for _ in range(3)] for _ in range(3)]

        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == '.':
                    continue
                x = int(b)-1
                if row_has[i][x] or col_has[j][x] or sub_box_has[i//3][j//3][x]:
                    return False
                row_has[i][x] = col_has[j][x] = sub_box_has[i//3][j//3][x] = True
        return True

        reverse_board = [list(row) for row in zip(*board)]
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        for i in range(9):
            rows[i].append([x for x in board[i]])
            cols[i].append([x for x in reverse_board[i]])

# @lc code=end



#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#


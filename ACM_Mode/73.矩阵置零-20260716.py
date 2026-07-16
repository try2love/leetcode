#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30404
#
# [73] 矩阵置零
# 6:11 ACM AC
from typing import List
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 参考答案：不使用额外空间
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]

        for i in range(1, m):
            for j in range(n):  # 如果第一列包含 0，那么 matrix[0][0] 会置为 0
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 注意顺序，先改第一列，再改第一行（避免把 matrix[0][0] 从 1 改成 0 影响判断）
        if matrix[0][0] == 0:  # 替换原来的 first_col_has_zero
            for row in matrix:
                row[0] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        return
        
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]  # 记录第一行是否包含 0
        first_col_has_zero = any(row[0] == 0 for row in matrix)  # 记录第一列是否包含 0

        # 用第一列 matrix[i][0] 保存 row_has_zero[i]
        # 用第一行 matrix[0][j] 保存 col_has_zero[j]
        for i in range(1, m):  # 无需遍历第一行，如果 matrix[0][j] 本身是 0，那么相当于 col_has_zero[j] 已经是 True
            for j in range(1, n):  # 无需遍历第一列，如果 matrix[i][0] 本身是 0，那么相当于 row_has_zero[i] 已经是 True
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 相当于 row_has_zero[i] = True
                    matrix[0][j] = 0  # 相当于 col_has_zero[j] = True

        for i in range(1, m):  # 跳过第一行，留到最后修改
            for j in range(1, n):  # 跳过第一列，留到最后修改
                if matrix[i][0] == 0 or matrix[0][j] == 0:  # i 行或 j 列有 0
                    matrix[i][j] = 0

        # 如果第一列一开始就包含 0，那么把第一列全变成 0
        if first_col_has_zero:
            for row in matrix:
                row[0] = 0

        # 如果第一行一开始就包含 0，那么把第一行全变成 0
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        return
        
        # 参考答案：额外数组
        row_has_zero = [0 in row for row in matrix]
        col_has_zero = [0 in col for col in zip(*matrix)]
        for i, row0 in enumerate(row_has_zero):
            for j, col0 in enumerate(col_has_zero):
                if row0 or col0:
                    matrix[i][j] = 0
        return
        
        # 需要记录最原始的0的位置，需要遍历一次
        origin = []
        for i, line in enumerate(matrix):
            for j, x in enumerate(line):
                if x == 0:
                    origin.append([i, j])
        for item in origin:
            i, j = item
            matrix[i] = [0] * len(matrix[0])
            for row in range(len(matrix)):
                matrix[row][j] = 0
        return
        
# @lc code=end

import json
import sys
matrix = json.loads(sys.stdin.readline().strip())
sol = Solution()
sol.setZeroes(matrix)
print(matrix)

#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#


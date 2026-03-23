#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30401
#
# [73] 矩阵置零
# 11:28 ACM AC 但是感觉很暴力，时间和空间上都是
from typing import List
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # -----参考答案------
        # m+n空间复杂度：额外的True，False数组
        row_has_zero = [0 in row for row in matrix]
        col_has_zero = [0 in col for col in zip(*matrix)]

        for i, row0 in enumerate(row_has_zero):
            for j,col0 in enumerate(col_has_zero):
                if row0 or col0:
                    matrix[i][j] = 0

        # 使用常数变量，存储第一行、第一列是否有0元素，然后把所有0元素的信息迁移到0行和0列
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]
        first_col_has_zero = any(row[0] == 0 for row in matrix)

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_has_zero:
            matrix[0] = [0]*n
        if first_col_has_zero:
            for row in matrix:
                row[0] = 0
        # -----参考答案------

        # m, n = len(matrix), len(matrix[0])
        # 可以dfs，下面的结果一定错误了，没有判断
        # def dfs(i:int, j:int):
        #     for col in range(n):
        #         if matrix[i][col] == 0:
        #             dfs(i,col)
        #         else:
        #             matrix[i][col] = 0
        #     for row in range(m):
        #         if matrix[row][j] == 0:
        #             dfs(row,j)
        #         else:
        #             matrix[row][j] = 0
        # for i,row in enumerate(matrix):
        #     for j,x in enumerate(row):
        #         if x==0:
        #             dfs(i,j)

        # tmp = []
        # for i, row in enumerate(matrix):
        #     for j, x in enumerate(row):
        #         if x == 0:
        #             tmp.append((i,j))
        # for i,j in tmp:
        #     # i行j列全部为0
        #     for col in range(n):
        #         matrix[i][col] = 0
        #     for row in range(m):
        #         matrix[row][j] = 0

# @lc code=end

import sys
data = sys.stdin.readlines()
grid = []
for line in data:
    grid.append(list(map(int, line.strip().split())))

sol = Solution()
sol.setZeroes(grid)
print(grid)


#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#


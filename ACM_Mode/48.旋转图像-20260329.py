#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30402
#
# [48] 旋转图像
# 15:10 ACM AC 本来想用zip(*matrix)实现优雅的转置的，但是这样得到的是tuple，需要看答案怎么做
from typing import List
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # -----参考答案------
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()

        for i, row in enumerate(matrix):
            for j in range(i+1, n):
                row[j], matrix[j][i] = matrix[j][i], row[j]
            row.reverse()

        # zip的做法新开辟了空间，是不符合题意的
        matrix[:] = [list(r) for r in zip(*matrix[::-1])]
        # -----参考答案------


        # matrix = list(zip(*matrix))
        # print(matrix)
        # for row in matrix:
        #     row[:] = row[::-1]
        # 先转置，再逆置
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row[:] = row[::-1]
        return

# @lc code=end
import sys
# 问题：如何一下把这个输入转为二维矩阵呢[[1,2,3],[4,5,6],[7,8,9]]
data = input()
grid = []
tmp = []
for i in range(len(data)):
    if data[i] == "]":
        grid.append(tmp)
        tmp = []
    elif data[i] in [",", "["]:
        continue
    else:
        tmp.append(int(data[i]))
sol = Solution()
print(grid[:-1])
sol.rotate(grid[:-1])
print(grid)



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#


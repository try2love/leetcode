#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30404
#
# [48] 旋转图像
#
from typing import List
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 忘记怎么做了
        n = len(matrix)
        for i, row in enumerate(matrix):
            for j in range(i+1, n):
                row[j], matrix[j][i] = matrix[j][i], row[j]
            row.reverse()
        return

        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#


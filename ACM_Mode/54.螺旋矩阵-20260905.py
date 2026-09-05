#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30404
#
# [54] 螺旋矩阵
# 14:36 ACM AC
from typing import List
# @lc code=start
pos = ((0,1), (1,0), (0,-1), (-1,0))
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 参考答案
        m, n = len(matrix), len(matrix[0])
        ans = []
        size = m*n
        i, j, di = 0, -1, 0
        while len(ans) < size:
            dx, dy = pos[di]
            for _ in range(n): # 走n步，n会减少
                i += dx
                j += dy
                ans.append(matrix[i][j])
            di = (di+1)%4
            m, n = n, m-1
        return ans


        m, n = len(matrix), len(matrix[0])
        ans = [0] * (m*n)
        row, col = 0,0
        direction = 0
        idx = 0
        while 0<=row<m and 0<=col<n and matrix[row][col] != -101:
            ans[idx] = matrix[row][col]
            matrix[row][col] = -101
            idx += 1
            row += pos[direction][0]
            col += pos[direction][1]
            if idx < (m*n) and (row >= m or row < 0 or col >=n or col < 0) or (0<=row<m and 0<=col<n and matrix[row][col] == -101):
                row -= pos[direction][0]
                col -= pos[direction][1]
                direction = (direction+1)%4
                row += pos[direction][0]
                col += pos[direction][1]
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#


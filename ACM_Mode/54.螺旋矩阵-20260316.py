#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30400
#
# [54] 螺旋矩阵
# 21:42 ACM AC，已经初见成效了，知道用位置矩阵了。但是搞笑的是，更新col的时候写错了
# 0x3f的做法真是神了 这辈子学不来
from typing import List
# @lc code=start
class Solution:
    directions = ((0,1), (1,0), (0,-1), (-1,0)) # 右下左上
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 因为数字有范围，所以可以原地修改矩阵，用101表示被访问
        m, n = len(matrix), len(matrix[0])
        bias = 0 # 更换方向的次数
        row, col = 0, 0
        ans = [matrix[row][col]]
        matrix[row][col] = 101
        while len(ans)!=m*n:
            nxt_row, nxt_col = self.directions[bias%4]
            tmp_row = nxt_row + row
            tmp_col = nxt_col + col
            if tmp_row>=m or tmp_row<0 or tmp_col>=n or tmp_col<0 or matrix[tmp_row][tmp_col]==101:
                bias += 1
                nxt_row, nxt_col = self.directions[bias%4]
                row = nxt_row + row
                col = nxt_col + col
            else:
                row, col = tmp_row, tmp_col
            ans.append(matrix[row][col])
            matrix[row][col] = 101
        return ans

DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右下左上

class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        size = m * n
        ans = []
        i, j, di = 0, -1, 0  # 从 (0, -1) 开始
        while len(ans) < size:
            dx, dy = DIRS[di]
            for _ in range(n):  # 走 n 步（注意 n 会减少）
                i += dx
                j += dy  # 先走一步
                ans.append(matrix[i][j])  # 再加入答案
            di = (di + 1) % 4  # 右转 90°
            n, m = m - 1, n  # 减少后面的循环次数（步数）
        return ans
# @lc code=end
import sys
data = sys.stdin.readlines()
matrix = []
for line in data:
    matrix.append(list(map(int, line.strip().split())))
sol = Solution()
print(sol.spiralOrder(matrix))

#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#


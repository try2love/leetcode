#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30404
#
# [54] 螺旋矩阵
# 19:09 ACM AC
from typing import List
# @lc code=start
DIRS = (0,1), (1,0), (0,-1), (-1,0)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 参考答案
        m, n = len(matrix), len(matrix[0])
        ans = []
        size = m*n
        i, j, di = 0, -1, 0
        while len(ans) < size:
            dx, dy = DIRS[di]
            for _ in range(n): # 走n步，n会减少
                i += dx
                j += dy
                ans.append(matrix[i][j])
            di = (di+1)%4
            m, n = n, m-1
        return ans


        i = j = di = 0
        for _ in range(m*n):
            ans.append(matrix[i][j])
            matrix[i][j] = None
            x, y = i + DIRS[di][0], j + DIRS[di][1]
            if x < 0 or x>=m or y<0 or y>=n or matrix[x][y] is None:
                di = (di+1)%4
            i += DIRS[di][0]
            j += DIRS[di][1]
        return ans

        # 四个方向
        directions = [(0,1), (1,0), (0,-1), (-1,0)] # 右下左上
        m, n = len(matrix), len(matrix[0])
        visited = [[0]*n for _ in range(m)]
        direction = 0
        i = j = 0
        ans = [matrix[i][j]]
        visited[i][j] = 1
        while len(ans) != m*n:
            i += directions[direction][0]
            j += directions[direction][1]
            if i>=m or j>=n or i<0 or j<0 or visited[i][j]:
                i -= directions[direction][0]
                j -= directions[direction][1]
                direction = (direction + 1) % 4
                i += directions[direction][0]
                j += directions[direction][1]
            ans.append(matrix[i][j])
            visited[i][j] = 1
        return ans

# @lc code=end

import json
import sys
sol = Solution()
matrix = json.loads(sys.stdin.readline().strip())
ans = sol.spiralOrder(matrix)
print(ans)

#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#


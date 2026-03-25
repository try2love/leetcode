#
# @lc app=leetcode.cn id=240 lang=python3
# @lcpr version=30401
#
# [240] 搜索二维矩阵 II
# 3:09 AC 6:10 ACM AC
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 本质上就是右上角逐渐缩小范围
        row = 0
        col = len(matrix[0])-1
        while row < len(matrix) and col > -1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
# @lc code=end

import sys
lines = sys.stdin.readlines()
grid = []
for line in lines:
    grid.append(list(map(int, line.strip().split())))
target = eval(input())
sol = Solution()
print(sol.searchMatrix(grid, target))
#
# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#


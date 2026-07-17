#
# @lc app=leetcode.cn id=240 lang=python3
# @lcpr version=30404
#
# [240] 搜索二维矩阵 II
# 4:05 ACM AC
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        while row < m and col > -1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

# @lc code=end

import json
import sys
sol = Solution()
matrix = json.loads(sys.stdin.readline().strip())
target = eval(input())
print(sol.searchMatrix(matrix, target))


#
# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#


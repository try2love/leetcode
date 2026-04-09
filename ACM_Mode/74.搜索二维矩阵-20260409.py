#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30403
#
# [74] 搜索二维矩阵
# 4:27 ACM AC
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # -----参考答案------
        left, right = -1, m*n
        while left+1 < right:
            mid = (left + right) // 2
            x = matrix[mid//n][mid%n]
            if x == target:
                return True
            if x < target:
                left = mid
            else:
                right = mid
        return False
        # -----参考答案------

        row, col = 0, n-1
        while row < m and col > -1:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False

# @lc code=end
import sys
import json
matrix = json.loads(sys.stdin.readline().strip())
target = eval(input())
sol = Solution()
print(sol.searchMatrix(matrix, target))


#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#


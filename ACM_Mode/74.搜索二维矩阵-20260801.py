#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30404
#
# [74] 搜索二维矩阵
# 1:52 ACM AC
from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 参考
        left, right = 0, m*n-1
        while left < right:
            mid = (left+right)//2
            x = matrix[mid//n][mid%n]
            if x == target:
                return True
            elif x > target:
                right = mid
            else:
                left = mid+1
        return matrix[left//n][left%n] == target

        row, col = 0, n-1
        while row < m and col > -1:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True
        return False
        
# @lc code=end



#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30404
#
# [118] 杨辉三角
# 5:17 ACM AC
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 参考答案
        c = [[1] * (i+1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                c[i][j] = c[i-1][j-1] + c[i-1][j]
        return c

        ans = [[1]*(i+1) for i in range(numRows)]
        for row in range(2, numRows):
            for col in range(1,row):
                ans[row][col] = ans[row-1][col-1] + ans[row-1][col]
        return ans

# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30400
#
# [118] 杨辉三角
# 6:07 AC
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows==1:
            return ans
        for i in range(2, numRows+1):
            ans.append([1]*i)
            for j in range(1,i-1):
                ans[-1][j] = ans[-2][j-1] + ans[-2][j]
        return ans

# @lc code=end

numRows = eval(input())
sol = Solution()
print(sol.generate(numRows))
               

#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


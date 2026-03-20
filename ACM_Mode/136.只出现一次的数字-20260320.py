#
# @lc app=leetcode.cn id=136 lang=python3
# @lcpr version=30400
#
# [136] 只出现一次的数字
# 9:57 ACM AC，但是总感觉题目要求的常数空间复杂度没有满足，因为最坏情况下，空间复杂度为o(n//2)
from typing import List
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 线性时间复杂度和常数空间吗，有点意思
        cnt = set()
        for x in nums:
            if x in cnt:
                cnt.remove(x)
            else:
                cnt.add(x)
        return cnt.pop()
# @lc code=end

import sys
data = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.singleNumber(data))


#
# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


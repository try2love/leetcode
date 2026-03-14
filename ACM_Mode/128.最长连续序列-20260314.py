#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30400
#
# [128] 最长连续序列
# 4:17 AC 5:00 ACM AC
from typing import List

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set(nums)
        nums = list(hash_map)
        ans = 0
        for x in nums:
            if x-1 in hash_map:
                continue
            y = x+1
            while y in hash_map:
                y += 1
            ans = max(ans, y-x)
        return ans
# @lc code=end

import sys
data = sys.stdin.readline().strip().split()
data = [int(x) for x in data]
sol = Solution()
ans = sol.longestConsecutive(data)
print(ans)
#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30400
#
# [1] 两数之和
#
from collections import defaultdict
from typing import List
# # @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = defaultdict(int)
        for i,x in enumerate(nums):
            cnt[x] = i
        for i, x in enumerate(nums):
            if cnt[target-x]>i:
                return [i, cnt[target-x]]
        return [-1,-1]
# # @lc code=end
import sys

for line in sys.stdin:

    a, b = map(int, line.strip().split())
    result = Solution()

    print(result)


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

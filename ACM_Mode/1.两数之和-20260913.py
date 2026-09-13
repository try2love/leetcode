#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30404
#
# [1] 两数之和
# 2:48 ACM AC
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 参考答案
        idx = {}
        for j,x in enumerate(nums):
            if target-x in idx:
                return [idx[target-x], j]
            idx[x] = j

        for i,x in enumerate(nums):
            for j in range(i+1, len(nums)):
                if x + nums[j] == target:
                    return [i, j]

        pos = defaultdict(int)
        for idx, x in enumerate(nums):
            if target - x in pos:
                return [pos[target-x], idx]
            pos[x] = idx


# @lc code=end



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


#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30404
#
# [209] 长度最小的子数组
# 5:49 ACM AC
from typing import List
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 参考答案
        n = len(nums)
        ans = n+1
        s = left = 0
        for right, x in enumerate(nums):
            s += x
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right-left+1)
        return ans if ans <= n else 0

        n = len(nums)
        left = right = 0
        # 蠕动法
        if sum(nums) < target:
            return 0
        ans = n
        total = 0
        for right in range(n):
            total += nums[right]
            while total >= target and left <= right:
                ans = min(ans, right-left+1)
                total -= nums[left]
                left += 1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#


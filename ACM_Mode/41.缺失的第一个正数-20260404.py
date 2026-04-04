#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30402
#
# [41] 缺失的第一个正数
# 30:05 ACM AC，但是写的很勉强，beats 5.07 % of python3 submissions
from typing import List
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # -----参考答案------
        n = len(nums)
        for i in range(n):
            # 如果学生的学号在[1,n]但是没有在正确的座位上
            while 1<=nums[i]<=n and nums[nums[i]-1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        # 找第一个学号和座位编号不匹配的学生
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        # 学生都在正确座位上
        return n+1
        # -----参考答案------

        # 最小正整数，一定在len之内
        n = len(nums)
        for idx in range(n):
            x = nums[idx]
            if x > n or x <= 0 or idx+1==x:
                continue
            while nums[idx]!=idx+1 or nums[idx]>n or nums[idx]<=0:
                next_idx = nums[idx]-1
                if 0<=next_idx<n and nums[next_idx]!=nums[idx]:
                    nums[idx], nums[next_idx] = nums[next_idx], nums[idx]
                else:
                    break
        ans = 1
        for x in nums:
            if x == ans:
                ans += 1
        return ans
# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.firstMissingPositive(nums))

#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#


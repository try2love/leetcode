#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30404
#
# [15] 三数之和
# 23:25 ACM AC
from collections import Counter
# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 参考答案
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[-2] + nums[-1] < 0:
                continue
            j = i+1
            k = n-1
            while j < k:
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
        return ans
        
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if len(ans) and ans[-1][0] == nums[i]:
                continue
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if len(ans) and ans[-1][0] == nums[i] and ans[-1][1] == nums[left]:
                    left += 1
                    continue
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return ans
# @lc code=end

import json
import sys
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.threeSum(nums))


#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#


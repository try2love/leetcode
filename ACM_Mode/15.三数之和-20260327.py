#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30401
#
# [15] 三数之和
# 15:30,没有A出来
from collections import Counter
# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # -----参考答案------
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            x = nums[i]
            if i>0 and x==nums[i-1]:
                continue
            if x+nums[i+1]+nums[i+2] > 0:
                break
            if x + nums[-2] + nums[-1] < 0:
                continue
            j = i+1
            k = n-1
            while j<k:
                s = x+nums[j] + nums[k]
                if s>0:
                    k -= 1
                elif s<0:
                    j += 1
                else:
                    if j==i+1 or nums[j] != nums[j-1]:
                        ans.append([x, nums[j], nums[k]])
                    j += 1
                    k -= 1
        return ans


        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2):
            x = nums[i]
            if i > 0 and x==nums[i-1]:
                continue
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[-2] + nums[-1] < 0:
                continue
            j = i+1
            k = n-1
            while j<k:
                s = x + nums[j] + nums[k]
                if s>0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k -= 1
        return ans
        # -----参考答案------

        # ans = []
        # # 本质上是两数之和，目标为-x，关键是如何去重？
        # cnt = Counter(nums)
        # for x in list(set(nums)):
        #     cnt[x] -= 1
        #     # 找两数之和
        #     for y in cnt:
        #         if cnt[y] == 0:
        #             continue
        #         cnt[y] -= 1
        #         if cnt[-x-y]!=0:
        #             tmp = sorted([x,y,-x-y])
        #             if tmp not in ans:
        #                 ans.append(tmp)
        #         cnt[y] += 1
        #     cnt[x] += 1
        # return ans
# @lc code=end

import sys
nums = list(map(int, sys.stdin.readline().strip().split()))
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


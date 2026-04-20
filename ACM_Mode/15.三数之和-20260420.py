#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30403
#
# [15] 三数之和
# 26:58，仍然没有AC，要么去重错误，要么超时
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
            if i > 0 and x == nums[i-1]:
                continue
            if x + nums[i+1] + nums[i+1] > 0:
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
            while j < k:
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j]==nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
        return ans
        # -----参考答案------

        ans = []
        nums.sort()
        pre = set()
        # 哈希表
        hash_map = Counter()
        for idx, x in enumerate(nums):
            if x < 0:
                hash_map[x] += 1
                pre.add(x)
                continue
            target = -x
            for p in pre:
                if target == 2*p and hash_map[p]==1:
                    continue
                if hash_map[target-p]:
                    cur = sorted([x, p, target-p])
                    ans.append(cur)
            hash_map[x] += 1
            pre.add(x)
        return [list(t) for t in set(tuple(i) for i in ans)]
        

# @lc code=end

import sys
import json
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


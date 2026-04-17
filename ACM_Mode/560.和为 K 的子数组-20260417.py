#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30403
#
# [560] 和为 K 的子数组
# 25:20，遇到bad case，拼尽全力无法战胜
from typing import List
from collections import Counter, defaultdict
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # -----参考答案------
        cnt = defaultdict(int)
        ans = s = 0
        for x in nums:
            cnt[s] += 1
            s += x
            ans += cnt[s-k]
        return ans

        cnt = defaultdict(int)
        cnt[0] = 1 # s[0]=0单独统计
        ans = s = 0
        for x in nums:
            s += x
            ans += cnt[s-k]
            cnt[s] += 1
        return ans

        s = [0] * (len(nums) + 1)
        for i,x in enumerate(nums):
            s[i+1] = s[i] + x
        cnt = defaultdict(int)
        ans = 0
        for sj in s:
            ans += cnt[sj-k]
            cnt[sj] += 1
        return ans
        # -----参考答案------

        # 连续非空，是不是滑动窗口好一些呢？
        # 前缀和 bad case: [-1,-1,1],k=0
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        prefix_sum = [0]*(len(nums)+1)
        # prefix_sum[0] = nums[0]
        ans = 0
        for idx in range(len(nums)):
            prefix_sum[idx] = prefix_sum[idx-1] + nums[idx]
        # prefix_sum = set(prefix_sum)
        cnt =Counter(prefix_sum)
        for x in prefix_sum[1::-1]:
            cnt[x] -= 1
            if x == k:
                ans += 1
                continue
            if cnt[x - k] > 0:
                cnt[x - k] -= 1
                ans += 1
        return ans

# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
k = eval(input())
sol = Solution()
print(sol.subarraySum(nums, k))

#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#


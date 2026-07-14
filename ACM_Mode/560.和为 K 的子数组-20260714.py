#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30404
#
# [560] 和为 K 的子数组
# 17:25 ACM AC
from typing import List
from collections import Counter, defaultdict
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 参考答案
        cnt = defaultdict(int)
        ans = s = 0
        for x in nums:
            cnt[s] += 1
            s += x
            ans += cnt[s-k]
        return ans

        cnt = defaultdict(int)
        cnt[0] = 1
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
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans
        
        # 连续非空则滑动窗口
        # 滑动窗口本质还是on2，得用前缀和，再来个哈希表
        pre_sum = [0] * (len(nums)+1)
        cnt = Counter()
        for idx, x in enumerate(nums):
            pre_sum[idx+1] = pre_sum[idx] + x
            cnt[pre_sum[idx+1]] += 1
        ans = 0
        for i in range(len(pre_sum)):
            x = pre_sum[i]
            if x in cnt and i!=0:
                cnt[x] -= 1
            ans += cnt[k+x]
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


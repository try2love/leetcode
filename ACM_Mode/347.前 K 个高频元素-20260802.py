#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30404
#
# [347] 前 K 个高频元素
# 10:21 ACM AC 办法不优雅
from typing import List
from collections import defaultdict, Counter
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 参考答案
        cnt = Counter(nums)
        max_cnt = max(cnt.values())
        buckets = [[] for _ in range(max_cnt+1)]
        for x,c in cnt.items():
            buckets[c].append(x)
        ans = []
        for bucket in reversed(buckets):
            ans += bucket
            if len(ans) == k:
                return ans
        return ans

        cnt = defaultdict(int)
        for x in nums:
            if x in cnt:
                cnt[x] += 1
            else:
                cnt[x] = 1
        target = list(cnt.values())
        print(target)
        target.sort()
        target = target[len(target)-k:]
        target = list(set(target))
        new_cnt = {}
        for key,val in cnt.items():
            if val in new_cnt:
                new_cnt[val].append(key)
            else:
                new_cnt[val] = [key]
        ans = []
        for val in target:
            ans.extend(new_cnt[val])
        return ans

        
# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
k = eval(input())
sol = Solution()
print(sol.topKFrequent(nums, k))

#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,3,1,3,2]\n2\n
# @lcpr case=end

#


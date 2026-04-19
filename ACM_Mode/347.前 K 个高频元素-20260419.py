#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30403
#
# [347] 前 K 个高频元素
# 9:13 ACM AC
from typing import List
from collections import Counter
from math import inf
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # -----参考答案------
        cnt = Counter(nums)
        max_cnt = max(cnt.values())
        buckets = [[] for _ in range(max_cnt+1)] # 相同元素放一个桶里面
        for x, c in cnt.items():
            buckets[c].append(x)
        # 倒排
        ans = []
        for bucket in reversed(buckets):
            ans += bucket
            if len(ans) == k:
                return ans
        return ans
        # -----参考答案------

        cnt = Counter(nums)
        ans = []
        ans_val = []
        cur_min = inf
        cur_idx = 0
        for key in cnt:
            val = cnt[key]
            if len(ans) < k:
                ans.append(key)
                ans_val.append(val)
                if cur_min > val:
                    cur_min = val
                    cur_idx = len(ans)-1
            else:
                if val > cur_min:
                    ans[cur_idx] = key
                    ans_val[cur_idx] = val
                    cur_min = min(ans_val)
                    cur_idx = ans_val.index(cur_min)
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


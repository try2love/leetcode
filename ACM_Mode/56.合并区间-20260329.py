#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30402
#
# [56] 合并区间
# 4:53 ACM AC
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # -----参考答案------
        intervals.sort(key=lambda p: p[0])
        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], p[1])
            else:
                ans.append(p)
        return ans
        # -----参考答案------
        
        intervals.sort(key=lambda x: x[0])
        ans = []
        left, right = intervals[0]
        for i in range(1, len(intervals)):
            l, r = intervals[i]
            if l <= right:
                right = max(right, r)
            else:
                ans.append([left, right])
                left = l
                right = r
        ans.append([left, right])
        return ans
# @lc code=end

import json
data = input()
intervals = json.loads(data)
sol = Solution()
print(sol.merge(intervals))

#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,7],[1,4]]\n
# @lcpr case=end

#


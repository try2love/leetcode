#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30404
#
# [56] 合并区间
# 9:02 ACM AC
from typing import List
from math import inf
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 参考答案
        intervals.sort(key=lambda p:p[0])
        n = len(intervals)
        ans = []
        left, right = inf, -inf
        for i, (l, r) in enumerate(intervals):
            left = min(left, l)
            right = max(right, r)
            if i == n-1 or intervals[i+1][0] > right:
                ans.append([left, right])
                left = inf
        return ans
        
        intervals.sort(key=lambda p: p[0])
        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], p[1])
            else:
                ans.append(p)
        return ans
        
        if len(intervals) == 0:
            return []
        intervals.sort() # 忘记sort怎么设置key了
        ans = [intervals[0]]
        for it in intervals[1:]:
            x, y = it
            if ans[-1][1] <= y and ans[-1][1] >= x:
                ans[-1][1] = y
            elif ans[-1][1] >= y:
                continue
            else:
                ans.append(it)
        return ans

# @lc code=end
import sys
import json
intervals = json.loads(sys.stdin.readline().strip())
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


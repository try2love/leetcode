#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30404
#
# [56] 合并区间
# 6:44 ACM AC
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
        for i, (l,r) in enumerate(intervals):
            left = min(left, l)
            right = max(right, r)
            if i==n-1 or intervals[i+1][0] > right:
                ans.append([left, right])
                left = inf
        return ans

        intervals.sort(key=lambda p:p[0])
        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], p[1])
            else:
                ans.append(p)
        return ans

        # intervals.sort(key=lambda x[0]: x in intervals)
        intervals.sort()
        ans = []
        start,end = intervals[0]
        i = 1
        while i < len(intervals):
            if intervals[i][0] > end:
                ans.append([start, end])
                start, end = intervals[i]
            else:
                end = max(end, intervals[i][1])
            i += 1
        if len(ans)==0 or ans[-1][0] != start:
            ans.append([start,end])
        return ans
        
# @lc code=end



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


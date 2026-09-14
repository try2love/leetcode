#
# @lc app=leetcode.cn id=57 lang=python3
# @lcpr version=30404
#
# [57] 插入区间
# 21:08 ACM AC
from typing import List
from math import inf
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 参考答案
        st, ed = newInterval
        ans = []
        insert = False
        for s,e in intervals:
            if ed<s:
                if not insert:
                    ans.append([st,ed])
                    insert=True
                ans.append([s,e])
            elif e<st:
                ans.append([s,e])
            else:
                st=min(st,s)
                ed = max(ed,e)
        if not insert:
            ans.append([st,ed])
        return ans

        def merge(intervals):
            intervals.sort()
            ans = [intervals[0]]
            for s,e in intervals[1:]:
                if ans[-1][1] < s:
                    ans.append([s,e])
                else:
                    ans[-1][1] = max(ans[-1][1],e)
            return ans
        intervals.append(newInterval)
        return merge(intervals)

        ans = []
        if len(intervals) == 0:
            return [newInterval]
        left, right = newInterval
        if left > intervals[-1][1]:
            ans = intervals
            ans.append(newInterval)
            return ans
        if right < intervals[0][0]:
            ans = [newInterval]
            ans += intervals
            return ans
        isEnd = False
        for idx, (start, end) in enumerate(intervals):
            if end < newInterval[0]:
                ans.append([start, end])
            elif start > newInterval[1]:
                ans.append([left, right])
                ans.extend(intervals[idx:])
                isEnd = True
                break
            else:
                left = min(left, start)
                right = max(right, end)
        if not isEnd:
            ans.append([left, right])
        return ans

# @lc code=end
intervals = [[1,5]]

newInterval = [2,3]
sol = Solution()
print(sol.insert(intervals, newInterval))


#
# @lcpr case=start
# [[1,3],[6,9]]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=452 lang=python3
# @lcpr version=30404
#
# [452] 用最少数量的箭引爆气球
# 9:10 放弃思考
from typing import List
from math import inf
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 参考答案
        points.sort(key=lambda p:p[1]) # 按照右端点从小到大排列
        ans = 0
        pre = -inf
        for start, end in points:
            if start > pre:
                ans += 1
                pre = end
        return ans

        # ans = 0
        # points.sort(key=lambda p:p[0])
        # left, right = inf, -inf
        # for idx, (x,y) in enumerate(points):
        #     if x <= left
        
# @lc code=end



#
# @lcpr case=start
# [[10,16],[2,8],[1,6],[7,12]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,4],[5,6],[7,8]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[4,5]]\n
# @lcpr case=end

#


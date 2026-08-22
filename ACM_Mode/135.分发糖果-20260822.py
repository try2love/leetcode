#
# @lc app=leetcode.cn id=135 lang=python3
# @lcpr version=30404
#
# [135] 分发糖果
# 2:00 直接看答案
from typing import List
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 感觉是先找到最小的分数，钉死为1，然后往两边扩展
        # 参考答案
        ans = n = len(ratings)
        i = 0
        while i < n:
            start = i-1 if i>0 and ratings[i-1] < ratings[i] else i
            while i+1 < n and ratings[i] < ratings[i+1]:
                i += 1
            top = i
            while i+1 < n and ratings[i] > ratings[i+1]:
                i += 1
            inc = top - start
            dec = i - top
            ans += (inc * (inc-1) + dec * (dec-1)) // 2 + max(inc, dec)
            i += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,0,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

#


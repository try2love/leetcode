#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30404
#
# [128] 最长连续序列
# 3:55 ACM AC
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 参考答案
        st = set(nums)
        m = len(st)
        ans = 0
        for x in st:
            if x-1 in st:
                continue
            y = x+1
            while y in st:
                y += 1
            ans = max(ans, y-x)
            if ans * 2 >= m:
                break
        return ans

        st = set(nums)
        ans = 0
        for x in st:
            if x-1 in st:
                continue
            y = x+1
            while y in st:
                y += 1
            ans = max(ans, y-x)
        return ans

        st = set(nums)
        ans = 0
        for x in st:
            if x-1 in st:
                continue
            y = x+1
            l = 1
            while y in st:
                l += 1
                y += 1
            ans = max(l, ans)
        return ans
# @lc code=end



#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#


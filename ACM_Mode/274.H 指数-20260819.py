#
# @lc app=leetcode.cn id=274 lang=python3
# @lcpr version=30404
#
# [274] H 指数
# 8:25 ACM AC
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 参考答案
        n = len(citations)
        cnt = [0] * (n+1)
        for c in citations:
            cnt[min(c, n)] += 1
        s = 0
        for i in range(n, -1, -1):
            s += cnt[i]
            if s >= i:
                return i

        if len(citations) == 1 and citations[0] > 0:
            return 1
        if min(citations) >= len(citations):
            return len(citations)
        nums = [0]*(max(citations)+1)
        for x in citations:
            nums[x] += 1
        left = 0
        right = len(citations)
        ans = 0
        while left < right:
            mid = (left+right)//2
            if sum(nums[mid:]) >=  mid:
                left = mid+1
                ans = mid
            else:
                right = mid
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [3,0,6,1,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,1]\n
# @lcpr case=end

#


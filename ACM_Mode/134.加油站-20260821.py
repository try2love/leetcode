#
# @lc app=leetcode.cn id=134 lang=python3
# @lcpr version=30404
#
# [134] 加油站
# 13:20 35/40 cases passed (N/A)
from  typing import List
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 参考答案
        ans = min_s = s =0
        for i, (g,c) in enumerate(zip(gas, cost)):
            s += g-c
            if s < min_s:
                ans = i+1
                min_s = s
        return -1 if s<0 else ans

        candidate = [idx for idx in range(len(gas)) if gas[idx]-cost[idx]>=0]
        n = len(gas)
        for start in candidate:
            cur = gas[start]
            j = start
            while cur >=0 and j < n + start:
                j += 1
                cur -= cost[(j-1)%n]
                if cur >= 0:
                    cur += gas[j%n]
            if cur >=0 and j== n+start:
                return start
        return -1
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n[3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#


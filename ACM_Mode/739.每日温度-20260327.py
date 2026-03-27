#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30401
#
# [739] 每日温度
# 4:19 ACM AC
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调栈
        st = []
        ans = [0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while st and temperatures[st[-1]] < t:
                idx = st.pop()
                ans[idx] = i-idx
            st.append(i)
        return ans

# @lc code=end
import sys
temperatures = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.dailyTemperatures(temperatures))

#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#


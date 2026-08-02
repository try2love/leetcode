#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30404
#
# [739] 每日温度
# 4:41 ACM AC
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 单调递减栈
        st = []
        ans = [0] * len(temperatures)
        for idx, t in enumerate(temperatures):
            if not st:
                st.append(idx)
                continue
            while len(st):
                if t > temperatures[st[-1]]:
                    pre = st.pop()
                    ans[pre] = idx - pre
                else:
                    break
            st.append(idx)
        return ans
        
# @lc code=end



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


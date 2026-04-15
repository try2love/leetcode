#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30403
#
# [239] 滑动窗口最大值
# 7:39 ACM AC
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # -----参考答案------
        ans = [0] * (len(nums) - k + 1)
        q = deque()
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            left = i - k + 1
            if q[0] < left:
                q.popleft()
            if left >= 0:
                ans[left] = nums[q[0]]
        return ans
        # -----参考答案------
        
        # 单调栈
        st = deque([])
        for i in range(k):
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            st.append(i)
        ans = [nums[st[0]]]
        for i in range(k, len(nums)):
            if st and st[0] < i-k+1:
                st.popleft()
            while st and nums[st[-1]] < nums[i]:
                st.pop()
            st.append(i)
            ans.append(nums[st[0]])
        return ans

# @lc code=end
import sys
import json
nums = json.loads(sys.stdin.readline().strip())
k = eval(input())
sol = Solution()
print(sol.maxSlidingWindow(nums, k))


#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30403
#
# [42] 接雨水
# 27:30 没做出来，已经没有思路了。看答案
from typing import List
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # -----参考答案------
        # 方法3:单调栈
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and height[st[-1]] <= h:
                bottom_h = height[st.pop()]
                if not st: # 栈为空
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h # 面积的高
                ans += dh * (i-left-1)
            st.append(i)
        return ans

        # 方法2:相向双指针
        ans = pre_max = suf_max = 0
        left, right = 0, len(height)-1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans

        # 方法1:前后缀分解
        n = len(height)
        pre_max = [0]*n # pre_max[i]表示从height[0]到height[i]的最大值
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])
        suf_max = [0]*n # suf_max[i]表示从height[i]到height[n-1]的最大值
        suf_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])
        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h
        return ans

        # -----参考答案------

        # 维护一个右侧最大的idx列表
        tmp = [0]*len(height)
        for i in range(len(height)-1, -1, -1):
            tmp[i] = max(tmp[i], height[i])
        ans = 0
        for i in range(len(height)):
            ans += min(height[i], tmp[i])

        # 单调栈做法，维护右侧最大高度，所以需要单调递减栈
        if len(height) == 0:
            return 0
        ans = 0
        st = [0]
        for i in range(1, len(height)):
            if len(st):
                if height[i] >= height[st[0]]:
                    ans += (height[st[0]] * (i-st[0]-1))
                    st.clear()
                    st.append(i)
                else:
                    ans -= height[i]
                    st.append(i)
            else:
                st.append(i)
        return ans

# @lc code=end

import sys
import json
height = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.trap(height))

#
# @lcpr case=start
# [0,1,0,2,1,0,1,3,2,1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,2,0,3,2,5]\n
# @lcpr case=end

#


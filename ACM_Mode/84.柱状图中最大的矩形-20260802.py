#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30404
#
# [84] 柱状图中最大的矩形
# 2:04 没想起来做法，只知道左右往中间赶
from typing import List
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调递增栈，遇到一个较小的，可以算出前一个面积。宽需再次获取栈顶元素
        heights = [0] + heights + [0]
        stack = []
        ans = 0
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]: 
                # 对于重复元素，会多次求面积，最后会算到最大面积
                # [9,8,7,7,7,7,6]. 6这里会分别与前面四个7算出最大面积
                dh = heights[stack.pop()]
                dw = i - stack[-1] - 1
                ans = max(ans, dh * dw)
        
            stack.append(i)
        return ans

        # 一次遍历
        heights.append(-1)
        st = [-1]
        ans = 0
        for right, h in enumerate(heights):
            while len(st) > 1 and heights[st[-1]] >= h:
                i = st.pop()
                left = st[-1]
                ans = max(ans, heights[i] * (right-left-1))
            st.append(right)
        return ans

        # 枚举高度
        n = len(heights)
        left = [-1] * n
        st = [] # 单调递增站
        # 两次遍历
        right = [n]*n
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                right[st.pop()] = i
            if st:
                left[i] = st[-1]
            st.append(i)
        ans = 0
        for h, l, r in zip(heights,left,right):
            ans = max(ans, h*(r-l-1))
        return ans
        # 三次遍历
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        right = [n] * n
        st.clear()
        for i in range(n-1, -1, -1):
            h = heights[i]
            while st and heights[st[-1]] >= h:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        ans = 0
        for h,l,r in zip(heights, left, right):
            ans = max(ans, h*(r-l-1))
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#


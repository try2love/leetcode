#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30400
#
# [84] 柱状图中最大的矩形
# 耗时18min14s无法战胜，WA了好几次，已经完全忘记这题的思路了，我用的双指针。
# 什么时候用到单调栈呢？
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

        # heights.append(-1)
        # st = [-1]
        # ans = 0
        # for right, h in enumerate(heights):
        #     while len(st)>1 and heights[st[-1]] >=h:
        #         i = st.pop()
        #         left = st[-1]
        #         ans = max(ans, heights[i] * (right - left - 1))
        #     st.append(right)
        # return ans

        # n = len(heights)
        # left = [-1] * n
        # right = [n] * n
        # st = []
        # for i, h in enumerate(heights):
        #     while st and heights[st[-1]] >= h:
        #         right[st.pop()] = i
        #     if st:
        #         left[i] = st[-1]
        #     st.append(i)
        # ans = 0
        # for h, l, r in zip(heights, left, right):
        #     ans = max(ans, h*(r-l+1))
        # return ans


        # n = len(heights)
        # left = [-1] * n
        # st = []
        # for i,h in enumerate(heights):
        #     while st and heights[st[-1]] >= h:
        #         st.pop()
        #     if st:
        #         left[i] = st[-1]
        #     st.append(i)

        # right = [n]*n
        # st.clear()
        # for i in range(n-1, -1, -1):
        #     h = heights[i]
        #     while st and heights[st[-1]] >= h:
        #         st.pop()
        #     if st:
        #         right[i] = st[-1]
        #     st.append(i)

        # ans = 0
        # for h,l,r in zip(heights, left, right):
        #     ans = max(ans, h*(r-l-1))
        # return ans

        # # 双指针问题
        # if len(heights) == 0:
        #     return 0
        # for i,x in enumerate(heights):
        #     if x == 0:
        #         return max(self.largestRectangleArea(heights[:i]), self.largestRectangleArea(heights[i+1:]))
        # left, right = 0, len(heights)-1
        # ans = heights[left]
        # while left <= right:
        #     ans = max(min(heights[left:right+1]) * (right-left+1), ans)
        #     if heights[left] < heights[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return ans

# @lc code=end

import sys
data = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
ans = sol.largestRectangleArea(data)
print(ans)



#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#


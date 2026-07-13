#
# @lc app=leetcode.cn id=42 lang=python3
# @lcpr version=30404
#
# [42] 接雨水
# 18:38 ACM AC 只想起来了比较笨的竖向计算方案
from typing import List
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 参考答案
        # 单调栈
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and height[st[-1]] <= h:
                bottom_h = height[st.pop()]
                if not st:
                    break
                left = st[-1]
                dh = min(height[left], h) - bottom_h
                ans += dh * (i - left - 1)
            st.append(i)
        return ans

        # 一次遍历
        ans = pre_max = suf_max = 0
        left, right = 0, len(height) - 1
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

        # 前后缀分解
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])
        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])
        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h
        return ans

        # 对于每一个元素，找它自己的左边最大和右边最大
        # 元素i，左边最大left_max ， 右边最大 right_max
        # 能盛水：height[i] < left_max and height[i] < right_max
        # 盛水量：(min(left_max, right_max) - height[i]) * 1
        # 相当于是每一个蓝条竖着计算
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        ans = 0
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        # print(left_max)
        # print(right_max)
        for i in range(len(height)):
            tmp = min(left_max[i], right_max[i]) - height[i]
            if tmp > 0:
                ans += tmp
        return ans

# @lc code=end

import json
import sys
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


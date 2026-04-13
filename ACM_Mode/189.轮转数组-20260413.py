#
# @lc app=leetcode.cn id=189 lang=python3
# @lcpr version=30403
#
# [189] 轮转数组
# 3:31 ACM AC
from typing import List
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # -----参考答案------
        def reverse(i:int, j:int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)
        k %= n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        # -----参考答案------

        # 方法1
        # n = len(nums)
        # k = k%n
        # start = n - k
        # nums[:] = nums[start:] + nums[:start]

        # 方法2:转队列
        # from collections import deque
        # nums = deque(nums)
        # n = len(nums)
        # k = k%n
        # for _ in range(k):
        #     tmp = nums.popleft()
        #     nums.append(tmp)
        # nums[:] = list(nums)

# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
k = eval(input())
sol = Solution()
sol.rotate(nums, k)
print(nums)

#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-1,-100,3,99]\n2\n
# @lcpr case=end

#


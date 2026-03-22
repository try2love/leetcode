#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30401
#
# [75] 颜色分类
# 10:01 ACM AC，问题在于没想出来空间1的做法
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # -----参考答案------
        p0 = p1 = 0
        for i,x in enumerate(nums):
            nums[i] = 2
            if x <= 1:
                nums[p1] = 1
                p1 += 1
            if x == 0:
                nums[p0] = 0
                p0 += 1

        # 三指针参考答案
        idx, p0, p2 = 0, 0, len(nums)-1
        while idx <= p2:
            if nums[idx] == 0:
                nums[p0], nums[idx] = nums[idx], nums[p0]
                p0 += 1
                idx += 1
            elif nums[idx] == 2:
                nums[p2], nums[idx] = nums[idx], nums[p2]
                p2 -= 1
            else:
                idx += 1

        # -----参考答案------

        # # 最直观：cnt计数，空间o(n)
        # cnt = Counter(nums)
        # nums[:] = [0] * cnt[0] + [1] * cnt[1] + [2] * cnt[2]

        # 能不能优化？三指针交换
        # zero, one, two = 0, 0, len(nums)-1
        # while two > max(zero, one):
        #     while nums[two] == 2:
        #         two -= 1
        #     while nums[zero] == 0:
        #         zero += 1
        #         one += 1
        #     nums[zero], nums[two] = nums[two], nums[zero]
        #     if nums[two] == 2:
        #         two -= 1
        #     if nums[zero] == 0:
        #         zero += 1
        #         one += 1
        #     else:
        #         one += 1

    
# @lc code=end
import sys
nums = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
sol.sortColors(nums)
print(nums)


#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#


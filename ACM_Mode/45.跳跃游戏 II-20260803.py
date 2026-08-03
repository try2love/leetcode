#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30404
#
# [45] 跳跃游戏 II
# 10:36 ACM AC
from typing import List
from math import inf
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 参考答案
        ans = 0
        cur_end = 0
        next_end = 0
        for i in range(len(nums)-1):
            next_end = max(next_end, i+nums[i])
            if i == cur_end:
                cur_end = next_end
                ans += 1
        return ans

        ans = [inf] * len(nums)
        ans[0] = 0
        for idx, x in enumerate(nums):
            for j in range(idx+1, min(idx+x+1, len(nums))):
                ans[j] = min(ans[j], ans[idx]+1)
        return ans[-1]
        
# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.jump(nums))

#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#


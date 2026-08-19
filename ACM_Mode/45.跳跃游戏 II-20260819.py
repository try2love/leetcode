#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30404
#
# [45] 跳跃游戏 II
# 3:07 ACM AC
from typing import List
from functools import cache
from math import inf
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 参考
        ans = 0
        cur_end = 0
        next_end = 0
        for i in range(len(nums)-1):
            next_end = max(next_end, i+nums[i])
            if i == cur_end:
                cur_end = next_end
                ans += 1
        return ans

        @cache
        def dfs(i:int):
            if i>= len(nums)-1:
                return 0
            if nums[i] == 0:
                return inf
            return min([dfs(i+x) for x in range(1, nums[i]+1)])+1
        return dfs(0)
        
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#


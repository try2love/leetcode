#
# @lc app=leetcode.cn id=169 lang=python3
# @lcpr version=30404
#
# [169] 多数元素
# 2:23 ACm AC
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 擂台赛
        cur = nums[0]
        hp = 1
        for x in nums[1:]:
            if x != cur:
                hp -= 1
                if hp == 0:
                    cur = x
                    hp = 1
            else:
                hp += 1
        return cur
        
# @lc code=end



#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#


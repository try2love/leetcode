#
# @lc app=leetcode.cn id=169 lang=python3
# @lcpr version=30404
#
# [169] 多数元素
# 4:22 ACM AC
from typing import List
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # cankao
        ans = hp = 0
        for x in nums:
            if hp==0:
                ans, hp =x, 1
            else:
                hp += 1 if x==ans else -1
        return ans

        # 这个是真擂台赛了
        ans = nums[0]
        hp = 1
        for x in nums[1:]:
            if ans == x:
                hp += 1
            else:
                hp -= 1
            if hp <= 0:
                ans = x
                hp = 1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#


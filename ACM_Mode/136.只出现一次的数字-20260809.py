#
# @lc app=leetcode.cn id=136 lang=python3
# @lcpr version=30404
#
# [136] 只出现一次的数字
#
from typing import List
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 印象里是打擂台赛
        # 具体忘记怎么做了
        # 参考：异或
        ans = 0
        for x in nums:
            ans = ans ^ x
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


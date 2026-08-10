#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30404
#
# [287] 寻找重复数
# 3:00 直接看答案
from typing import List

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 参考答案
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        head = 0
        while slow != head:
            slow = nums[slow]
            head = nums[head]
        return slow
        
# @lc code=end



#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#


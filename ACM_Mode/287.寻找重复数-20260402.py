#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30402
#
# [287] 寻找重复数
# 想到的思路是使用异或，但是异或是用来特殊场景的：
# 除了某个元素只出现一次以外，其余每个元素均出现两次
# 这个题要用的是环形链表
from operator import xor
from typing import List
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # -----参考答案------
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # 等价于fast = fast.next.next
            if fast == slow:
                break
        head = 0
        while slow != head:
            slow = nums[slow]
            head = nums[head]
        return slow
        # -----参考答案------

        # 异或操作
        ans = 0
        for x in nums:
            ans = xor(ans, x)
        return ans
        
# @lc code=end
import sys
nums = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
print(sol.findDuplicate(nums))

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


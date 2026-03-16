#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30400
#
# [141] 环形链表
# 4:13 直接快慢指针结束。问题是while的循环判断，几次提交都少了点东西 8:52 ACM AC
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# 判断有换问题直接快慢指针
class Solution:
    def build_list(self, nums, pos):
        if len(nums) == 0:
            return None
        head = cur = ListNode(nums[0])
        tmp = None
        for i in range(1, len(nums)):
            if i==pos:
                cur.next = tmp = ListNode(nums[i])
            else:
                cur.next = ListNode(nums[i])
            cur = cur.next
        cur.next = tmp
        return head

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next and fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                return True
        return False
# @lc code=end

import sys
data = sys.stdin.readline()
nums = list(map(int, data.strip().split()))
pos = eval(input())

sol = Solution()
head = sol.build_list(nums, pos)
print(sol.hasCycle(head))

#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#


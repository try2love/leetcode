#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30404
#
# [142] 环形链表 II
# 耗时13:30，放弃
from typing import Optional
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def judge(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 参考答案
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None
        
        if not self.judge(head):
            return None
        # slow: x = a+n*b+c, fast:2x=a+m*b+c
        # ask: a = (m-2n) * b - c
        # 耗时13:30，放弃

# @lc code=end



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


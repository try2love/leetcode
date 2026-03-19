#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30400
#
# [206] 反转链表
# 5:39 迭代 花了5分钟，没写出来递归 15:50 ACM AC

from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归：尾插法得到反转链表
        if head is None or head.next is None:
            return head
        rev_head = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return rev_head

        # if head is None:
        #     return None
        # dummy = ListNode(next=head)
        # self.reverseList(head.next).next = head
        # head.next = dummy.next.next
        # return dummy.next


        # 头插法得到反转链表
        # dummy = ListNode()
        # cur = head
        # while cur:
        #     nxt = cur.next
        #     cur.next = dummy.next
        #     dummy.next = cur
        #     cur = nxt
        # return dummy.next

    def build_ListNode(self, nums:List[int]):
        dummy = ListNode()
        cur = dummy
        for x in nums:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next
    
    def print_ListNode(self, head:Optional[ListNode]):
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans
# @lc code=end

import sys
data = list(map(int, sys.stdin.readline().strip().split()))
sol = Solution()
head = sol.build_ListNode(data)
r_head = sol.reverseList(head)
print(sol.print_ListNode(r_head))
#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


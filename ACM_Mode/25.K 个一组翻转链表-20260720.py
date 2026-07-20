#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30404
#
# [25] K 个一组翻转链表
# 13:14 没写出来，但是有思路
from typing import Optional
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseAll(self, head: Optional[ListNode]):
        if head is None or head.next is None:
            return head
        tmp = self.reverseAll(head.next)
        tmp.next = head
        head.next = None
        return tmp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 参考答案
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        p0 = dummy = ListNode(next=head)
        pre = None
        cur = head

        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next

        # 错误解法
        end = head
        if head is None: # 怎么体现出来k个连续非空
            return head
        for _ in range(k-1):
            if not end:
                return head
            end = end.next
        start = head
        tmp = end.next
        end.next = None
        self.reverseAll(start)
        start.next = self.reverseKGroup(tmp, k)
        return end
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#


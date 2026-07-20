#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30404
#
# [24] 两两交换链表中的节点
# 6:11 ACM AC
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 参考答案：递归
        if head is None or head.next is None:
            return head
        node1 = head
        node2 = head.next
        node3 = node2.next
    
        node1.next = self.swapPairs(node3)
        node2.next = node1
        return node2
        
        if not head or head.next is None:
            return head
        cur = dummt = ListNode(0, head)
        a = head
        b = head.next
        while b:
            tmp = b.next
            cur.next = b
            b.next = a
            a.next = tmp
            cur = a
            a = tmp
            if a is None or a.next is None:
                break
            b = a.next
        return dummt.next

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#


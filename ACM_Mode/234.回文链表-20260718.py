#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30404
#
# [234] 回文链表
# 4:04 开辟额外空间做法
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 参考答案：先本地反转，最后再反转回来
        mid = self.middleNode(head)
        head2 = h2 = self.reverseList(mid)
        while head2:
            if head.val != head2.val:
                self.reverseList(h2)
                return False
            head = head.next
            head2 = head2.next
        self.reverseList(h2)
        return True
        
        # 如何用o1的空间？暂时想不到

        
        # 最直观：开辟额外空间
        ans = []
        cur = head
        while cur:
            ans.append(cur.val)
            cur = cur.next
        return ans == ans[::-1]

# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#


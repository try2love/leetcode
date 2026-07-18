#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30404
#
# [2] 两数相加
# 5:18 ACM AC
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        # 参考答案
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        s = carry + l1.val + (l2.val if l2 else 0)
        l1.val = s % 10
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s//10)
        return l1
        
        if l1 is None and l2 is None and carry==0:
            return None
        s = carry
        if l1:
            s += l1.val
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next
        return ListNode(s%10, self.addTwoNumbers(l1, l2, s//10))
        
        cur = dummy = ListNode()
        pre = 0
        while l1 and l2:
            a = l1.val + l2.val + pre
            a, pre = a%10, a//10
            cur.next = ListNode(a)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            l2 = l1
        while l2:
            a = l2.val + pre
            a, pre = a%10, a//10
            cur.next = ListNode(a)
            cur = cur.next
            l2 = l2.next
        if pre != 0:
            cur.next = ListNode(pre)
        return dummy.next


# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#


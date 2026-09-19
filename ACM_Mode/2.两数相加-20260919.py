#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30404
#
# [2] 两数相加
# 12:52 ACM AC
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        s = carry + l1.val + (l2.val if l2 else 0)
        l1.val = s%10
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s//10)
        return l1

        if l1 is None and l2 is None and carry == 0:
            return None
        s = carry
        if l1:
            s += l1.val
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next
        return ListNode(s%10, self.addTwoNumbers(l1,l2,s//10))

    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 参考答案
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            s = carry
            if l1:
                s+= l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            cur.next = ListNode(s%10)
            carry = s//10
            cur = cur.next
        return dummy.next

        top = 0
        cur = ListNode(val=top)
        dummy = pre = ListNode(next=cur)
        
        h1, h2 = l1, l2
        while h1 and h2:
            cur.val += (h1.val+h2.val)
            if cur.val >= 10:
                top = cur.val // 10
                cur.val = cur.val % 10
            else:
                top = 0
            cur.next = ListNode(val=top)
            pre = pre.next
            cur = cur.next
            h1 = h1.next
            h2 = h2.next
        if h1:
            tmp = h1
        elif h2:
            tmp = h2
        else:
            tmp = None
        while tmp:
            cur.val += tmp.val
            if cur.val >= 10:
                top = cur.val // 10
                cur.val = cur.val % 10
            else:
                top = 0
            cur.next = ListNode(val=top)
            pre = pre.next
            cur = cur.next
            tmp = tmp.next
        if cur.val == 0:
            pre.next = None
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


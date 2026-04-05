#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30402
#
# [2] 两数相加
# 11:38 ACM AC，使用了新建链表的做法
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        # -----参考答案------
        if l1 is None and l2 is None and carry == 0:
            return None
        s = carry
        if l1:
            s += l1.val
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next
        return ListNode(s%10, self.addTwoNumbers(l1, l2, s//10))
    
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        s = carry + l1.val + (l2.val if l2 else 0)
        l1.val = s % 10
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, s//10)
        return l1
    
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            carry //= 10
            cur = cur.next
        return dummy.next
        # -----参考答案------

        # 新建链表写法
        cur = dummy = ListNode()
        pre = 0
        while l1 and l2:
            cur_val = l1.val + l2.val + pre
            pre = cur_val // 10
            cur.next = ListNode(cur_val%10)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        pre_node = cur
        cur = cur.next
        if pre == 0:
            return dummy.next
        while cur:
            cur.val, pre = (cur.val + pre) % 10, (cur.val+pre) // 10
            cur = cur.next
            pre_node = pre_node.next
        if pre!=0:
            pre_node.next = ListNode(pre)
        return dummy.next
# @lc code=end
import sys
import json
l1 = json.loads(sys.stdin.readline().strip())
l2 = json.loads(sys.stdin.readline().strip())
def build_listnode(nums):
    cur = dummy = ListNode()
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next
l1 = build_listnode(l1)
l2 = build_listnode(l2)

sol = Solution()
ans = sol.addTwoNumbers(l1, l2)
def print_listnode(root):
    ans = []
    while root:
        ans.append(root.val)
        root = root.next
    print(ans)
    return
print_listnode(ans)

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


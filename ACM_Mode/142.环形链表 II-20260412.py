#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30403
#
# [142] 环形链表 II
# 12:56 ACM AC，额外添加了flag来表征是否真正成环
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # -----参考答案------
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
        # -----参考答案------

        # 找环一般都是快慢指针
        if not head:
            return None
        flag = False
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = True
                break
        if not flag:
            return None # 没有环
        pos = head
        while pos != slow:
            pos = pos.next
            slow = slow.next
        return pos

# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
pos = eval(input())
def build_list(nums, pos):
    dummy = cur = ListNode(0)
    pre = None
    for idx, x in enumerate(nums):
        cur.next = ListNode(x)
        cur = cur.next
        if idx == pos:
            pre = cur
    cur.next = pre
    return dummy.next
head = build_list(nums, pos)
sol = Solution()
target = sol.detectCycle(head)
if target:
    print(target.val)
else:
    print("null")

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


#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30403
#
# [24] 两两交换链表中的节点
# 8:43 ACM AC
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # -----参考答案------
        # 迭代
        node0 = dummy = ListNode(next=head)
        node1 = head
        while node1 and node1.next:
            node2 = node1.next
            node3 = node2.next

            node0.next = node2
            node2.next = node1
            node1.next = node3

            node0 = node1
            node1 = node3
        return dummy.next
        # 递归
        if head is None or head.next is None:
            return head
        node1 = head
        node2 = head.next
        node3 = node2.next

        node1.next = self.swapPairs(node3)
        node2.next = node1
        return node2
        # -----参考答案------

        dummy = ListNode(next=head)
        pre = head
        if not pre:
            return dummy.next
        cur = pre.next
        if not cur:
            return dummy.next
        pre.next = cur.next
        cur.next = pre
        dummy.next = cur
        pre.next= self.swapPairs(pre.next)
        return dummy.next

# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
def build_list(nums):
    dummy = cur = ListNode()
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next
head = build_list(nums)

sol = Solution()
head = sol.swapPairs(head)
def print_list(head):
    ans = []
    while head:
        ans.append(head.val)
    print(ans)
print_list(head)


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


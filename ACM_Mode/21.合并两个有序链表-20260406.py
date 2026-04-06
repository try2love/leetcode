#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30402
#
# [21] 合并两个有序链表
# 7:16 ACM AC
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # -----参考答案------
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next

        if list1 is None: return list2
        if list2 is None: return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2
        # -----参考答案------

        if not list1:
            return list2
        if not list2:
            return list1
        dummy = pre = ListNode(next=list1)
        while list1 and list2:
            if list1.val <= list2.val:
                pre = pre.next
                list1 = list1.next
            else:
                tmp = list2.next
                list2.next = list1
                pre.next = list2
                list2 = tmp
                pre = pre.next
        if list1:
            pre.next = list1
        else:
            pre.next = list2
        return dummy.next

# @lc code=end
import sys
import json
nums1 = json.loads(sys.stdin.readline().strip())
nums2 = json.loads(sys.stdin.readline().strip())
def build_listnode(nums):
    dummy = cur = ListNode()
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next
l1 = build_listnode(nums1)
l2 = build_listnode(nums2)
sol = Solution()
new_head = sol.mergeTwoLists(l1, l2)
def print_list(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    print(ans)

print_list(new_head)

#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#


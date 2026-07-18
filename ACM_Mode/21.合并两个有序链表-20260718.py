#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30404
#
# [21] 合并两个有序链表
# 2:37 ACM AC
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 参考答案：递归（头插法）
        if list1 is None: return list2
        if list2 is None: return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2

        cur = dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
            cur.next = None
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return dummy.next

# @lc code=end



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


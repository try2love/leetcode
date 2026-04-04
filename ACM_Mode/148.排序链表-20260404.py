#
# @lc app=leetcode.cn id=148 lang=python3
# @lcpr version=30402
#
# [148] 排序链表
# 16:09 暴力新建链表方法实现ACM AC
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# -----参考答案------
class Solution:
    # 876. 链表的中间结点（快慢指针）
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            pre = slow  # 记录 slow 的前一个节点
            slow = slow.next
            fast = fast.next.next
        pre.next = None  # 断开 slow 的前一个节点和 slow 的连接
        return slow

    # 21. 合并两个有序链表（双指针）
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2  # 拼接剩余链表
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空或者只有一个节点，无需排序
        if head is None or head.next is None:
            return head
        # 找到中间节点 head2，并断开 head2 与其前一个节点的连接
        # 比如 head=[4,2,1,3]，那么 middleNode 调用结束后 head=[4,2] head2=[1,3]
        head2 = self.middleNode(head)
        # 分治
        head = self.sortList(head)
        head2 = self.sortList(head2)
        # 合并
        return self.mergeTwoLists(head, head2)
# -----参考答案------

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 可以直接暴力获取所有节点的值，然后新建链表并返回
        nums = []
        dummy = ListNode()
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        nums.sort()
        cur = dummy
        for x in nums:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next

        # 下面其实也挺暴力的，甚至还不如原来的新建链表方案，直接超时了
        if head is None:
            return None
        dummy = ListNode(next=head)
        cur = dummy.next
        latter = cur.next
        cur.next = None
        while latter:
            pre = dummy
            cur = dummy.next
            while cur and latter.val >= cur.val:
                cur = cur.next
                pre = pre.next
            tmp = latter.next
            latter.next = None
            pre.next = latter
            latter.next = cur
            latter = tmp
        return dummy.next

# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
def build_listnode(nums):
    dummy = cur = ListNode()
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next
head = build_listnode(nums)
sol = Solution()
def print_listnode(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    print(ans)
    return
print_listnode(sol.sortList(head))

#
# @lcpr case=start
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30404
#
# [206] 反转链表
# 4:50 核心AC 8:10 ACM AC
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 参考答案
        if head is None or head.next is None:
            return head
        rev_head = self.reverseList(head.next)
        tail = head.next
        tail.next = head
        head.next = None
        return rev_head
        
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
        
        # 头插法
        if head is None or head.next == None:
            return head
        dummy = ListNode(0)
        cur = head
        nxt = cur.next
        while nxt:
            cur.next = dummy.next
            dummy.next = cur
            cur = nxt
            nxt = nxt.next
        cur.next = dummy.next
        dummy.next = cur
        return dummy.next
            

# @lc code=end
import sys
import json
nums = json.loads(sys.stdin.readline().strip())
def build(nums):
    cur = dummy = ListNode()
    # 尾插法
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

head = build(nums)
sol = Solution()
head = sol.reverseList(head)

def print_list_node(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
    return ans

print(print_list_node(head))


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


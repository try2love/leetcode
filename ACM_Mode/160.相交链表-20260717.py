#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30404
#
# [160] 相交链表
# 14:19 核心AC 23:17 ACM AC
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 参考答案
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p
        
        lenA = 0
        lenB = 0
        head = headA
        while head:
            lenA += 1
            head = head.next
        head = headB
        while head:
            lenB += 1
            head = head.next
        if lenA > lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        diff = lenB - lenA
        for _ in range(diff):
            headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
        
        # A走完链路后走B；B走完链路后走A，如果节点一样，则就是有相交，没实现出来
        start1 = headA
        start2 = headB
        while start1 and start2:
            if start1 == start2:
                return start1
            start1 = start1.next
            start2 = start2.next
            if start1 == None:
                start1 = headB
            if start2 == None:
                start2 = headA
        return None

# @lc code=end
import sys
import json
intersectVal = eval(input())
listA = json.loads(sys.stdin.readline().strip())
listB = json.loads(sys.stdin.readline().strip())
skipA = eval(input())
skipB = eval(input())

def build_list_node(nums):
    dummy = head = ListNode(0)
    for x in nums:
        head.next = ListNode(x)
        head = head.next
    return dummy.next
sol = Solution()
headA = build_list_node(listA)
headB = build_list_node(listB)
if skipA == len(listA):
    ans = sol.getIntersectionNode(headA, headB)
else:
    target = headA
    for _ in range(skipA):
        target = target.next
    tmp = headB
    for _ in range(skipB-1):
        tmp = tmp.next
    to_del = tmp.next
    tmp.next = target
    del to_del
    ans = sol.getIntersectionNode(headA, headB)
if ans is None:
    print("No intersection")
else:
    print(f"Intersected at '{ans.val}'")

#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#


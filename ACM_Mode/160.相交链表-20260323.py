#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30401
#
# [160] 相交链表
# 4:39 核心AC 13:16 ACM AC
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # -----参考答案------
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

        # -----参考答案------

        tmp = headA
        m = n = 0
        while tmp:
            m += 1
            tmp = tmp.next
        tmp = headB
        while tmp:
            n += 1
            tmp = tmp.next
        if m<n: # 保证A长
            headA, headB = headB, headA
            m, n = n, m
        for _ in range(m-n):
            headA = headA.next
        while headA:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None

# @lc code=end

import sys
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))
skipA = eval(input())
skipB = eval(input())
def build_list(A,B,skipA,skipB):
    cur = dummyA = ListNode(0)
    link = None
    for idx,x in enumerate(A):
        cur.next = ListNode(x)
        cur = cur.next
        if idx == skipA:
            link = cur

    cur = dummyB = ListNode(0)
    for i in range(skipB):
        cur.next = ListNode(B[i])
    cur.next = link
    return dummyA.next, dummyB.next
headA, headB = build_list(A,B,skipA, skipB)
sol = Solution()
interval = sol.getIntersectionNode(headA, headB)
if interval is not None:
    print(f"Intersected at '{interval.val}'")
else:
    print("No intersection")

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


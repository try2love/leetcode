#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30400
#
# [19] 删除链表的倒数第 N 个结点
# 13:57 ACM AC，想了一会才想起来快慢指针
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 快慢指针
        fast = head
        slow = head
        dummy = pre = ListNode(next=head)
        for _ in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
            pre = pre.next
        tmp = slow.next
        pre.next = tmp
        slow.next = None
        del slow
        return dummy.next
    def build_list(self, nums):
        dummy = ListNode()
        cur = dummy
        for x in nums:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next
    def print_list(self, head):
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans
# @lc code=end

import sys
nums = list(map(int, sys.stdin.readline().strip().split()))
n = eval(input())
sol = Solution()
head = sol.build_list(nums)
print(sol.print_list(sol.removeNthFromEnd(head, n)))

#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#


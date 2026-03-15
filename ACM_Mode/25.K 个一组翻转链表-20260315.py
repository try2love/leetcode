#
# @lc app=leetcode.cn id=25 lang=python3
# @lcpr version=30400
#
# [25] K 个一组翻转链表
# 耗时23:24，踩坑：想到了用递归，但是递归边界忘记写了。然后是头插法的思路有些混乱。
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
class Solution:
    def build_list(self, nums):
        # 输入原生的nums，每一个都是str，需要转int
        head = ListNode()
        cur = head
        for x in nums:
            cur.next = ListNode(int(x))
            cur = cur.next
        return head.next
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1 or head==None:
            return head
        # 感觉是递归+快慢指针
        dummy = ListNode(next=head)
        start = end = dummy.next
        for _ in range(k-1):
            end = end.next
            if end is None:
                return dummy.next
        tmp = end.next
        # 头插法逆置
        end = start
        cur = start
        dummy.next = None
        while cur != tmp:
            start = start.next
            cur.next = dummy.next
            dummy.next = cur
            cur = start
        end.next = self.reverseKGroup(tmp,k)
        return dummy.next

    def print_list(self, head):
        ans = []
        while head!=None:
            ans.append(head.val)
            head = head.next
        return ans
# @lc code=end
import sys
data = sys.stdin.readline().strip().split()
k = eval(input())
sol = Solution()
head = sol.build_list(data)
head = sol.reverseKGroup(head,k)
print(sol.print_list(head))


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#


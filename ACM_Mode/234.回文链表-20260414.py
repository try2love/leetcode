#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30403
#
# [234] 回文链表
# 6:10 ACM AC
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# -----参考答案------
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
    def isPalindrome(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True

# -----参考答案------

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 遍历，获取数组，判断反转后是否一致即可
        # 如何用常数的空间复杂度呢？
        # 有没有可能，用str就是一种常数的空间复杂度呢
        s = ""
        while head:
            s += str(head.val)
            head = head.next
        return s==s[::-1]

# @lc code=end
import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
def build_list(nums):
    dummy = cur = ListNode()
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next
print(sol.isPalindrome(build_list(nums)))

#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30404
#
# [23] 合并 K 个升序链表
# 9:18 ACM AC
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
ListNode.__lt__ = lambda a,b : a.val < b.val
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwo(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwo(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwo(list1, list2.next)
            return list2
        return None

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 堆排序
        from heapq import heapify,heappop, heappush
        cur = dummy = ListNode()
        h = [head for head in lists if head]
        heapify(h)
        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next
        
        # 二路归并
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 0:
            return None
        while len(lists) > 1:
            tmp1 = lists.pop()
            tmp2 = lists.pop()
            lists.append(self.mergeTwo(tmp1, tmp2))
        return lists[0]
# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#


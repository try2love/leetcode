#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30400
#
# [23] 合并 K 个升序链表
# 10:39 核心模式AC，但是使用的是归并，时间复杂度高 19:00 ACM AC，仍然没有优化核心代码
from typing import List, Optional
from heapq import heapify, heappop, heappush
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
class Solution:
    def mergeTwo(self, list1, list2):
        dummy = ListNode()
        end = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                end.next = list1
                list1 = list1.next
            else:
                end.next = list2
                list2 = list2.next
            end = end.next
            end.next = None
        end.next = list1 if list1 else list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)
        if m==0:
            return None
        if m == 1:
            return lists[0]
        left = self.mergeKLists(lists[:m//2])
        right = self.mergeKLists(lists[m//2:])
        return self.mergeTwo(left, right)

        # 这个才是真的二路归并，通过step控制谁两个合并
        # step = 1
        # while step < m:
        #     for i in range(0, m-step, step*2):
        #         lists[i] = self.mergeTwo(lists[i], lists[i+step])
        #     step *= 2
        # return lists[0]

        # 堆排序，构建最小堆，堆顶为最小元素，维护cur保证尾插法
        # ListNode.__lt__ = lambda a,b: a.val < b.val
        # cur = dummy = ListNode()
        # h = [head for head in lists if head] # 只加入非空
        # heapify(h)
        # while h:
        #     node = heappop(h)
        #     if node.next:
        #         heappush(h, node.next)
        #     cur.next = node
        #     cur = cur.next
        # return dummy.next

        # 分治，二路归并
        # if len(lists) == 0:
        #     return None
        # elif len(lists)==1:
        #     return lists[0]
        # head1 = lists.pop()
        # head2 = lists.pop()
        # lists.append(self.mergeTwo(head1, head2))
        # return self.mergeKLists(lists)

    def build_list(self,nums):
        dummy = ListNode()
        end = dummy
        for x in nums:
            end.next = ListNode(x)
            end = end.next
        return dummy.next

    def print_list(self, head):
        ans = []
        while head:
            ans.append(head.val)
            # head = head.next
        return ans

# @lc code=end
import sys
import signal

sys.setrecursionlimit(200000)
data = sys.stdin.readlines()
datas = []
for line in data:
    datas.append(list(map(int, line.strip().split())))
lists = []
sol = Solution()
for nums in datas:
    lists.append(sol.build_list(nums))

def handler(signum, frame):
    raise TimeoutError("运行超时")
signal.signal(signal.SIGALRM, handler)
signal.alarm(2)

try:
    print(sol.print_list(sol.mergeKLists(lists)))
except TimeoutError as e:
    print(e)


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


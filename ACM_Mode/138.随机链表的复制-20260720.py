#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30404
#
# [138] 随机链表的复制
# 8:35 错误结果，直接看答案
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 参考答案
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur =  cur.next.next
        cur = dummy = Node(0, head)
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return dummy.next
        
        # 最直观：列表存储节点
        tmp_list = []
        rand_list = []
        while head:
            node = Node(head.val)
            rand_list.append(head.random) if head.random is not None else -1
            if len(tmp_list):
                tmp_list[-1].next = node
            head = head.next
            tmp_list.append(node)
        for idx, x in rand_list:
            if x == -1:
                continue
            tmp_list[idx].random = tmp_list[x]
        return tmp_list[0]
        

# @lc code=end



#
# @lcpr case=start
# [[7,null],[13,0],[11,4],[10,2],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,null],[3,0],[3,null]]\n
# @lcpr case=end

#


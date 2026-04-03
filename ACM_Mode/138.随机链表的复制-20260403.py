#
# @lc app=leetcode.cn id=138 lang=python3
# @lcpr version=30402
#
# [138] 随机链表的复制
# 28:19 ACM AC，感觉绕了好大一圈啊
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# @lc code=start

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # -----参考答案------
        # 复制每一个节点，把新节点直接插入原节点后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next
        # 遍历交错链表中的原链表节点
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 第一种，删除原链表节点
        cur = dummy = Node(0, head)
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return dummy.next
        # 第二种，把交错链表分离
        tail = dummy = Node(0, head)
        cur = head
        while cur:
            copy = cur.next
            tail.next = copy
            cur.next = copy.next
            cur = cur.next
            tail = tail.next
        return dummy.next
        # -----参考答案------
    
        tmp = []
        random_idx = []
        new_cur = dummy = Node(0)
        cur = head
        while cur:
            tmp_random = cur.random
            if tmp_random is not None:
                cur_rand = head
                idx = 0
                while cur_rand != tmp_random:
                    idx += 1
                    cur_rand = cur_rand.next
                random_idx.append(idx)
            else:
                random_idx.append(-1)
            tmp.append(Node(cur.val))
            new_cur.next = tmp[-1]
            new_cur = new_cur.next
            cur = cur.next
        cur = head
        new_cur = dummy.next
        cur_random_idx = 0

        while cur:
            real_idx = random_idx[cur_random_idx]
            new_cur.random = tmp[real_idx] if real_idx!=-1 else None
            cur = cur.next
            new_cur = new_cur.next
            cur_random_idx += 1
        return dummy.next
        
# @lc code=end

import sys
import json
def build_list_node(nums):
    tmp = []
    dummy = Node(0)
    cur = dummy
    for x in nums:
        tmp_node = Node(x[0])
        cur.next = tmp_node
        cur = cur.next
        tmp.append(cur)
    for i,x in enumerate(nums):
        if x[1] == None:
            continue
        tmp[i].random = tmp[int(x[1])]
    return dummy.next

def print_list_node(head):
    ans = []
    while head:
        ans.append([str(head.val), str(head.random.val) if head.random else "null"])
        head = head.next
    print(ans)
    return

head = json.loads(sys.stdin.readline().strip())
sol = Solution()
head = build_list_node(head)
new_head = sol.copyRandomList(head)
print_list_node(new_head)


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


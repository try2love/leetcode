#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30404
#
# [146] LRU 缓存
#

# @lc code=start
# class ListNode:
#     def __init__(self, val=0, pre=None,next=None):
#         self.val = val
#         self.pre = pre
#         self.next = next
from typing import Optional
class Node:
    __slots__ = 'prev', 'next', 'key', 'val'
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val

class LRUCache:
    # 本质双链表+哈希表
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.key_to_node = {}

    def get_node(self, key:int) -> Optional[Node]:
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.val = value
            return
        self.key_to_node[key] = node = Node(key, value)
        self.push_front(node)
        if len(self.key_to_node) > self.capacity:
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)

    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev
    def push_front(self, x:Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



#
# @lcpr case=start
# ["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]\n
# @lcpr case=end

#


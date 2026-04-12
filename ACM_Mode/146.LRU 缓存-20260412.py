#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30403
#
# [146] LRU 缓存
# 35:00，AMC AC，存在很多问题啊，最开始没有给节点添加key，导致出现了很多问题
from typing import Optional
# @lc code=start
# -----参考答案------
class Node:
    # 提高访问属性的速度，并节省内存
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()  # 哨兵节点
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    # 获取 key 对应的节点，同时把该节点移到链表头部
    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:  # 没有这本书
            return None
        node = self.key_to_node[key]  # 有这本书
        self.remove(node)  # 把这本书抽出来
        self.push_front(node)  # 放到最上面
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)  # get_node 会把对应节点移到链表头部
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)  # get_node 会把对应节点移到链表头部
        if node:  # 有这本书
            node.value = value  # 更新 value
            return
        self.key_to_node[key] = node = Node(key, value)  # 新书
        self.push_front(node)  # 放到最上面
        if len(self.key_to_node) > self.capacity:  # 书太多了
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # 去掉最后一本书

    # 删除一个节点（抽出一本书）
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    # 在链表头添加一个节点（把一本书放到最上面）
    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x
# -----参考答案------

class ListNode:
    def __init__(self, key:int=-1, val:int=-1, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:
    # 想象有一本书，因此使用双向链表+哈希表
    def __init__(self, capacity: int):
        self.dummy = ListNode()
        self.dummy.next = self.dummy
        self.dummy.pre = self.dummy
        self.hash_map = {}
        self.capacity = capacity

    def remove_node(self, node: Optional[ListNode]) -> None:
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.next = None

    def add_to_top(self, cur:Optional[ListNode]) -> None:
        # 把cur节点放到链表开头
        cur.next = self.dummy.next
        self.dummy.next = cur
        cur.next.pre = cur
        cur.pre = self.dummy

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.remove_node(node)
            self.add_to_top(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hash_map:
            if len(self.hash_map) >= self.capacity:
                removed = self.dummy.pre
                del self.hash_map[removed.key]
                self.remove_node(removed)
            node = ListNode(key,value)
            self.hash_map[key] = node
            self.add_to_top(self.hash_map[key])
        else:
            node = self.hash_map[key]
            node.val = value
            self.remove_node(node)
            self.add_to_top(node)
        

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


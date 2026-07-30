#
# @lc app=leetcode.cn id=208 lang=python3
# @lcpr version=30404
#
# [208] 实现 Trie (前缀树)
# 知道可以数组可以set实现，但是具体实现方式忘记了，是需要一个新的class吗

# @lc code=start
class Node:
    def __init__(self):
        self.son = [None for _ in range(26)]
        self.end = False

class Trie:

    def __init__(self):
        self.dummy = Node()

    def insert(self, word: str) -> None:
        cur = self.dummy
        for c in word:
            idx = ord(c) - ord('a')
            if cur.son[idx] is None:
                node = Node()
                cur.son[idx] = node
            cur = cur.son[idx]
        cur.end = True
        return

    def find(self, word: str) -> int:
        cur = self.dummy
        for c in word:
            idx = ord(c) - ord('a')
            if cur.son[idx] is None:
                return 0
            cur = cur.son[idx]
        return 1 if cur.end else 2

    def search(self, word: str) -> bool:
        return self.find(word)==1

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0

class Tree:
    def __init__(self):
        self.child = {} 
        self.isEnd = False

class Trie:

    def __init__(self):
        self.head = Tree()

    def insert(self, word: str) -> None:
        cur = self.head
        for ch in word:
            if ch in cur.child:
                cur = cur.child[ch]
            else:
                node = Tree()
                # cur.child.add(ch : node)
                cur.child[ch] = node
                cur = cur.child[ch]
        cur.isEnd = True

    def func_search(self, word:str) -> int:
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                return -1
            cur = cur.child[ch]
        if cur.isEnd == True:
            return 0
        else:
            return 1

    def search(self, word: str) -> bool:
        return self.func_search(word) == 0

    def startsWith(self, prefix: str) -> bool:
        return self.func_search(prefix) != -1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end



#
# @lcpr case=start
# ["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=208 lang=python3
# @lcpr version=30402
#
# [208] 实现 Trie (前缀树)
# 字典对象如何插入简直对？

# @lc code=start
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


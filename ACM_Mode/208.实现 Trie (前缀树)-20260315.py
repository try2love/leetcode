#
# @lc app=leetcode.cn id=208 lang=python3
# @lcpr version=30400
#
# [208] 实现 Trie (前缀树)
# 关键是选取什么样的数据结构来实现。
# 想起来了，是多叉树，逻辑上的26叉树，相当于小哈夫曼编码了
# 22:11 核心AC 39:54 ACM AC，但是还是要看一下别人怎么实现这个测试用例的。

# @lc code=start
class MultiTree:
    def __init__(self, letter="", isend=False):
        self.val = letter
        self.children = [None] * 26
        self.isend = isend

class Trie:
    def __init__(self):
        self.begin = MultiTree()

    def insert(self, word: str) -> None:
        chars = list(word)
        cur = self.begin
        for i, x in enumerate(chars):
            if cur.children[ord(x)-ord('a')] is None:
                cur.children[ord(x)-ord('a')] = MultiTree(x)
            cur = cur.children[ord(x)-ord('a')]
            if i==len(chars)-1:
                cur.isend = True

    def init_search(self, word: str):
        chars = list(word)
        cur = self.begin
        for i,x in enumerate(chars):
            if cur.children[ord(x)-ord('a')] is None:
                return 0
            cur = cur.children[ord(x)-ord('a')]
        return 1 if cur.isend else 2

    def search(self, word: str) -> bool:
        return self.init_search(word) == 1

    def startsWith(self, prefix: str) -> bool:
        return self.init_search(prefix) != 0
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
import sys
data = sys.stdin.readlines()
operations = data[0].split()
details = [[x] for x in data[1].split()]
times = len(details)
ans = []
trie = Trie()
ans.append(None)
for i in range(times):
    cur_operation = operations[i+1]
    cur_detail = details[i][0]
    match cur_operation:
        case "insert":
            trie.insert(cur_detail)
            ans.append(None)
        case "search":
            ans.append(trie.search(cur_detail))
        case "startsWith":
            ans.append(trie.startsWith(cur_detail))
print(ans)

#
# @lcpr case=start
# ["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]\n
# @lcpr case=end

#


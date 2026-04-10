#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30403
#
# [101] 对称二叉树
#
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:

    def isSameTree(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left,q.right) and self.isSameTree(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, root.right)

        # 对称过去看看是不是完全一致
        new_root = root
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            node.left, node.right = node.right, node.left
        dfs(new_root)
        return root == new_root

        # 还是只能想起来中序遍历对称，如果元素有相同的，就会有错误答案
        # bad case: [1,2,2,2,null,2]，返回了True
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return ans == ans[::-1]
            

# @lc code=end
import sys
from collections import deque
data_str = sys.stdin.readline().strip()
def build_tree(data_str:str) -> TreeNode:
    if not data_str or data_str=="null":
        return None
    nodes = data_str.replace('[','').replace(']','').split(',')
    nodes = [n.strip() for n in nodes]
    root = TreeNode(int(nodes[0]))
    q = deque([root])
    i = 1
    while q and i<len(nodes):
        cur = q.popleft()
        if i<len(nodes) and nodes[i] != "null":
            cur.left = TreeNode(int(nodes[i]))
            q.append(cur.left)
        i += 1
        if i<len(nodes) and nodes[i] != "null":
            cur.right = TreeNode(int(nodes[i]))
            q.append(cur.right)
        i += 1
    return root

root = build_tree(data_str)
sol = Solution()
print(sol.isSymmetric(root))

#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30403
#
# [114] 二叉树展开为链表
# 19:22 核心AC，但是花了挺大功夫，29:20 ACM AC
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    head = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # -----参考答案------
        # 头插法
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.head
        self.head = root
        return

        # 尾插法，需要修改函数的返回为Optional[TreeNode]
        if root is None:
            return None
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right)
        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None
        return right_tail or left_tail or root
        # -----参考答案------

        # 要求原地修改
        def dfs(node):
            if not node:
                return None
            # 最开始没有意识到应该dfs一下
            left = dfs(node.left)
            while left and left.right:
                left = left.right
            if left:
                # 这里当时也没意识到需要dfs
                left.right = dfs(node.right)
                node.right = node.left
                node.left = None
            else:
                # 当时忘记了处理右子树
                node.right = dfs(node.right)
            return node
        dfs(root)

# @lc code=end
import sys
from collections import deque
data_str = sys.stdin.readline().strip()
def build_tree(data_str:str):
    if not data_str or data_str=="null":
        return None
    nodes = data_str.replace('[','').replace(']','').split(',')
    nodes = [str(s) for s in nodes]
    root = TreeNode(val = int(nodes[0]))
    q = deque([root])
    idx = 1
    while q and idx < len(nodes):
        cur = q.popleft()
        if idx < len(nodes) and nodes[idx] != 'null':
            cur.left = TreeNode(int(nodes[idx]))
            q.append(cur.left)
        idx += 1
        if idx < len(nodes) and nodes[idx] != 'null':
            cur.right = TreeNode(int(nodes[idx]))
            q.append(cur.right)
        idx += 1
    return root
root = build_tree(data_str)
sol = Solution()
sol.flatten(root)

def print_tree(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur:
                ans.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                ans.append('null')
    end = len(ans)-1
    while end >= 0:
        if ans[end] == 'null':
            end -= 1
        else:
            break
    print(ans[:end+1])

print_tree(root)
#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


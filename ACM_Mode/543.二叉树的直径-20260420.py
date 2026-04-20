#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=30403
#
# [543] 二叉树的直径
# 10:33 核心 AC，16:03 ACM AC
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # -----参考答案------
        ans = 0
        def dfs(node):
            if node is None:
                return 0
            l_len = dfs(node.left)
            r_len = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_len+r_len)
            return max(l_len, r_len)+1
        dfs(root)
        return ans

        def dfs(node):
            if node is None:
                return -1
            l_len = dfs(node.left)+1
            r_len = dfs(node.right)+1
            nonlocal ans
            ans = max(ans, l_len + r_len)
            return max(l_len, r_len)
        dfs(root)
        return ans
        # -----参考答案------

        ans = 0
        def dfs(node: Optional[TreeNode]):
            if not node:
                return -1, -1
            l_l, l_r = dfs(node.left)
            r_l, r_r = dfs(node.right)
            left = max(l_l, l_r) + 1
            right = max(r_l, r_r)+1
            nonlocal ans
            ans = max(ans, left+right)
            return left, right
        dfs(root)
        return ans

# @lc code=end

import sys
from collections import deque
data_str = sys.stdin.readline().strip()

def build_tree(data_str: str):
    nodes = data_str.replace("[","").replace("]","").split(",")
    if nodes[0] == "null" or not nodes:
        return None
    root = TreeNode(int(nodes[0]))
    q = deque([root])
    idx = 1
    while q and idx < len(nodes):
        cur = q.popleft()
        if nodes[idx] != "null":
            cur.left = TreeNode(int(nodes[idx]))
            q.append(cur.left)
        idx += 1
        if nodes[idx] != "null":
            cur.right = TreeNode(int(nodes[idx]))
            q.append(cur.right)
        idx += 1
    return root
root = build_tree(data_str)
sol = Solution()
print(sol.diameterOfBinaryTree(root))

#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#


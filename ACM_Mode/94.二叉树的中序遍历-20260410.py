#
# @lc app=leetcode.cn id=94 lang=python3
# @lcpr version=30403
#
# [94] 二叉树的中序遍历
#
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return ans

# @lc code=end

import sys
import ast
from collections import deque
# nums = ast.literal_eval(sys.stdin.readline().strip())

# def build_tree(nums):
#     if len(nums)==0:
#         return None
#     root = TreeNode(int(nums[0]))
#     q = deque([root])
#     cur = dummy = TreeNode(left=root)
#     bias = 0
#     while q:
#         for i in range(len(q)):

# -----参考答案------
data_str = sys.stdin.readline().strip()
def build_tree(data_str:str):
    if not data_str or data_str == "null":
        return None
    nodes = data_str.replace('[', '').replace(']', '').split(',')
    nodes = [n.strip() for n in nodes]
    root = TreeNode(int(nodes[0]))
    q = deque([root])
    i = 1
    while q and i<len(nodes):
        cur = q.popleft()
        if i < len(nodes) and nodes[i] != "null":
            cur.left = TreeNode(int(nodes[i]))
            q.append(cur.left)
        i += 1
        if i < len(nodes) and nodes[i] != "null":
            cur.right = TreeNode(int(nodes[i]))
            q.append(cur.right)
        i += 1
    return root

root = build_tree(data_str)
sol = Solution()
print(sol.inorderTraversal(root))

#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,null,8,null,null,6,7,9]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#


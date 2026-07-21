#
# @lc app=leetcode.cn id=94 lang=python3
# @lcpr version=30404
#
# [94] 二叉树的中序遍历
# 5:13 核心 AC，递归
from typing import Optional, List
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # cankao 
        ans = []
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right is not root:
                    pre = pre.right
                if pre.right is None:
                    pre.right = root
                    root = root.left
                    continue
                pre.right = None
            ans.append(root.val)
            root = root.right
        return ans
        
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        ans = []
        dfs(root)
        return ans
        
        
        ans = []
        if root is None:
            return ans
        def dfs(node):
            if node.left:
                dfs(node.left)
            ans.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        return ans

# @lc code=end
import sys
import json
import queue
nums = json.loads(sys.stdin.readline().strip()) # list[str]
sol = Solution()
# def build_tree(nums):
#     if len(nums) == 0 or nums[0] == "null":
#         return None
#     q = queue()
#     dummy = TreeNode()
#     for x in nums:

from collections import deque
def build_tree(data_str):
    if not data_str or data_str == "null":
        return None
    nodes = data_str.replace('[', '').replace(']', '').split(',')
    nodes = [n.strip() for n in nodes]
    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        cur = queue.popleft()
        if i < len(nodes) and nodes[i] != "null":
            cur.left = TreeNode(int(nodes[i]))
            queue.append(cur.left)
        i += 1
        if i < len(nodes) and nodes[i] != "null":
            cur.right = TreeNode(int(nodes[i]))
            queue.append(cur.right)
        i += 1
    return root

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


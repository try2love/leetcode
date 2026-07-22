#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30404
#
# [226] 翻转二叉树
# 2:43 ACM AC
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归互换，先换底层
        if root is None or (root.left is None and root.right is None):
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# @lc code=end



#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


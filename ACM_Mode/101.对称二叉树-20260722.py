#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30404
#
# [101] 对称二叉树
# 8:19 ACm AC
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
    def revertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        root.left, root.right = self.revertTree(root.right), self.revertTree(root.left)
        return root

    def judge(self, root1, root2):
        # 判断两棵树节点的val是否一致
        if root1 and root2:
            if root1.val != root2.val:
                return False
            return self.judge(root1.left, root2.left) and self.judge(root1.right, root2.right)
        elif not root1 and not root2:
            return True
        return False

    def isSameTree(self, p, q):
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 参考答案：
        return self.isSameTree(root.left, root.right)

        # 可以把柚子树反转后，判断左右是否完全一致
        if root is None or (root.left is None and root.right is None):
            return True
        self.revertTree(root.right)
        return self.judge(root.left, root.right)
        

# @lc code=end



#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#


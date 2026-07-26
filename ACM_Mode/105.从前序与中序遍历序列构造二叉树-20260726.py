#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30404
#
# [105] 从前序与中序遍历序列构造二叉树
# 7:36
from typing import List, Optional
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 参考答案
        index =  {x: i for i,x in enumerate(inorder)}
        def dfs(pre_l:int, pre_r:int, in_l:int) -> Optional[TreeNode]:
            if pre_l == pre_r:
                return None
            left_size = index[preorder[pre_l]] - in_l
            left = dfs(pre_l + 1, pre_l+1+left_size, in_l)
            right = dfs(pre_l+1+left_size, pre_r, in_l+1+left_size)
            return TreeNode(preorder[pre_l], left, right)
        return dfs(0, len(preorder), 0)

        if len(preorder) == 0 or len(inorder) == 0:
            return None
        target = preorder[0]
        left = inorder.index(target)
        root = TreeNode(preorder[0], self.buildTree(preorder[1:left+1], inorder[:left]), self.buildTree(preorder[left+1:], inorder[left+1:]))
        return root
# @lc code=end



#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30404
#
# [98] 验证二叉搜索树
# 7:58 ACM AC
from typing import Optional, List
from collections import deque
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 二叉搜索树中序遍历有序
        nums = []
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            if node.left:
                dfs(node.left)
            nums.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)
        # print(nums)
        return len(nums) == len(set(nums)) and nums == sorted(nums)
        return nums == list(set(nums)) == sorted(nums)

        # if root is None:
        #     return True
        # if root.left and root.left.val >= root.val:
        #     return False
        # if root.right and root.right.val <= root.val:
        #     return False
        # return self.isValidBST(root.left) and self.isValidBST(root.right)
# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#


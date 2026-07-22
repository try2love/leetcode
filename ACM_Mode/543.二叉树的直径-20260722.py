#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=30404
#
# [543] 二叉树的直径
# 9:40 没写出来
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 参考
        ans = 0
        def dfs(node):
            if node is None:
                return 0
            l_len = dfs(node.left)
            r_len = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_len + r_len)
            return max(l_len, r_len) + 1
        dfs(root)
        return ans

        ans = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            l_len = dfs(node.left) + 1
            r_len = dfs(node.right) + 1
            nonlocal ans
            ans = max(ans, l_len+r_len)
            return max(l_len, r_len)
        dfs(root)
        return ans

        ans = 0
        if root is None:
            return ans
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0,0,0 # 左最大，右最大，经过当前节点的最大
            if node:
                left_l, left_r, left_m = dfs(node.left)
                right_l, right_r, right_m = dfs(node.right)
                left, right =  max(left_l, right_l), max(right_r, left_r)
                mid = left + right
                ans = max(ans, left_m, right_m, mid)
                return left, right, 


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#


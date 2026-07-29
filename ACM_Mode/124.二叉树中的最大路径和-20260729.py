#
# @lc app=leetcode.cn id=124 lang=python3
# @lcpr version=30404
#
# [124] 二叉树中的最大路径和
# 10:24, 55/96，没有AC
from typing import Optional
from math import inf
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 参考答案
        ans = -inf
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l_val = dfs(node.left)
            r_val = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_val+r_val+node.val)
            return max(max(l_val,r_val)+node.val, 0)
        dfs(root)
        return ans

        # 左路径，右路径，走当前node的路径
        ans = -inf
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return -inf, -inf, -inf
            if node.left is None and node.right is None:
                return node.val, node.val, node.val
            left_l, right_l, mid_l = dfs(node.left)
            left_r, right_r, mid_r = dfs(node.right)
            left = max(left_l, right_l)
            right = max(left_r, right_r)
            nonlocal ans
            mid = max(left+right+node.val, left+node.val, right+node.val, node.val)
            ans = max(mid_l, mid_r, mid)
            return left+node.val, right+node.val, mid
        a, b, c = dfs(root)
        ans = max(ans, a, b, c)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=124 lang=python3
# @lcpr version=30403
#
# [124] 二叉树中的最大路径和
# 20:20，只实现了58/96，此时遇到了bad case [-2,-1]，输出了0
from typing import Optional
from math import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # -----参考答案------
        ans = -inf
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0 # 没有节点，和为0
            l_val = dfs(node.left) # 左子树的最大链和
            r_val = dfs(node.right) # 右子树的最大链和
            nonlocal ans
            ans = max(ans, l_val+r_val+node.val) # 两条链拼接成路径
            return max(max(l_val, r_val)+node.val, 0) # 当前子树的最大链和
        dfs(root)
        return ans
        # -----参考答案------

        ans = -inf
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0, 0, 0 # 左子树上最大，右子树最大，经过当前节点的最大
            left_left, left_right, left_mid = dfs(node.left)
            left = max(left_left, left_right, left_mid)
            right_left, right_right, right_mid = dfs(node.right)
            right = max(right_left, right_right, right_mid)
            mid = left_mid - min(left_left, left_right) + right_mid - min(right_left, right_right) + node.val
            # 遇到bad case [2,-1]输出了1而不是2。因此添加
            mid = max(mid, node.val)
            nonlocal ans
            ans = max(ans, mid)
            # 下面两个if遇到了bad case [-3]，输出了0
            if node.left:
                ans = max(ans, left)
            if node.right:
                ans = max(ans, right)
            return left, right, mid
        dfs(root)
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


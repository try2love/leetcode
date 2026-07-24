#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30404
#
# [230] 二叉搜索树中第 K 小的元素
# 9:03 ACM AC
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 参考答案
        def dfs(node):
            if node is None:
                return -1
            left_res = dfs(node.left)
            if left_res != -1:
                return left_res
            nonlocal k
            k -= 1
            if k == 0:
                return node.val
            return dfs(node.right)
        return dfs(root)
        
        ans = 0
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal k, ans
            if node is None or k <= 0:
                return
            dfs(node.left)
            k -= 1
            if k == 0:
                ans = node.val
            dfs(node.right)
        dfs(root)
        return ans

        # 本质就是中序遍历，到第k个
        ans = -1
        cnt = 0
        def dfs(node: Optional[TreeNode]):
            nonlocal ans, cnt
            if node is None or cnt >= k:
                return
            if node.left:
                dfs(node.left)
            cnt += 1
            if cnt <= k:
                ans = node.val
            if node.right:
                dfs(node.right)
        dfs(root)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#


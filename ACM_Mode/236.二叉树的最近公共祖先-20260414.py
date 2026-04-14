#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30403
#
# [236] 二叉树的最近公共祖先
# 14:05 ACM AC 用了笨方法

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # -----参考答案------
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
        # -----参考答案------

        # 初步的想法：从root到p和root到q，使用回溯的方式构造两个链表
        # 然后访问链表，到不一致的地方的上一级就是最近公共祖先
        path1 = []
        path2 = []
        path = []
        def dfs(node: 'TreeNode', p, q):
            if node is None:
                return
            path.append(node)
            if node is p:
                path1[:] = path[:]
            if node is q:
                path2[:] = path[:]
            dfs(node.left, p, q)
            dfs(node.right, p, q)
            path.pop()
        dfs(root, p, q)
        # print([x.val for x in path1])
        # print([x.val for x in path2])
        for i in range(min(len(path1), len(path2))):
            if path1[i] != path2[i]:
                return path1[i-1]
        return path1[-1] if len(path1) < len(path2) else path2[-1]

# @lc code=end



#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#


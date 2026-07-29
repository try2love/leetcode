#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30404
#
# [236] 二叉树的最近公共祖先
# 16::41 ACM AC
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 参考答案
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

        # 最简单做法：两个list，记录俩节点的链路，两次遍历树
        if p==root or q==root:
            return root
        p_path = []
        q_path = []
        path = []
        def dfs(node):
            if node is None:
                return
            path.append(node)
            if node == p:
                nonlocal p_path
                p_path = path[:]
            if node == q:
                nonlocal q_path
                q_path = path[:]
            if len(p_path) and len(q_path):
                return
            dfs(node.left)
            dfs(node.right)
            path.pop()
        dfs(root)
        cur = 0
        ans = root
        while cur < min(len(p_path), len(q_path)):
            if p_path[cur] == q_path[cur]:
                ans = p_path[cur]
                cur += 1
            else:
                return ans
        return ans
            
        
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


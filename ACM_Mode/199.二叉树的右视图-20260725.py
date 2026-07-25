#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30404
#
# [199] 二叉树的右视图
# 8:20 ACM AC
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 参考答案
        ans = []
        def dfs(node, depth):
            if node is None:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root, 0)
        return ans
        
        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            ans.append(cur[-1].val)
            nxt = []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
        return ans
    
        # 本质是层序遍历，每一层的最后一个元素
        if root is None:
            return []
        ans = [root.val]
        q = deque([root])
        layer = deque([])
        while len(q):
            cur = q.popleft()
            if cur.left:
                layer.append(cur.left)
            if cur.right:
                layer.append(cur.right)
            if len(q) == 0 and len(layer):
                ans.append(layer[-1].val)
                q = layer
                layer = deque([])
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


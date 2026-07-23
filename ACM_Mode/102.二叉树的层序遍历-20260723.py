#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30404
#
# [102] 二叉树的层序遍历
# 8:46 ACM AC
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 参考答案
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(vals)
        return ans

        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
            ans.append(vals)
        return ans

        ans = []
        if root is None:
            return ans
        q = deque([root])
        ans.append([root.val])
        layer_ans = []
        tmp_q = deque([])
        while q:
            cur = q.popleft()
            if cur.left:
                tmp_q.append(cur.left)
                layer_ans.append(cur.left.val)
            if cur.right:
                tmp_q.append(cur.right)
                layer_ans.append(cur.right.val)
            if len(q) == 0 and len(layer_ans):
                ans.append(layer_ans[:])
                layer_ans = []
                q = tmp_q
                tmp_q = deque([])
        return ans

        
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


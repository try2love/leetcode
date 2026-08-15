#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30404
#
# [102] 二叉树的层序遍历
# 5:13 ACM AC
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, x=0, left=None, right=None):
        self.val = x
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
        # 参考答案：一个队列
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

        ans = []
        if not root:
            return ans
        layer = deque([root])
        tmp = deque([])
        layer_ans = []
        while layer:
            cur = layer.popleft()
            layer_ans.append(cur.val)
            if cur.left:
                tmp.append(cur.left)
            if cur.right:
                tmp.append(cur.right)
            if len(layer) == 0:
                ans.append(layer_ans[:])
                layer = tmp
                tmp = deque([])
                layer_ans = []
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


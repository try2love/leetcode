#
# @lc app=leetcode.cn id=114 lang=python3
# @lcpr version=30404
#
# [114] 二叉树展开为链表
# 21:35 94/225 cases passed (N/A)
# [1,2,null,3]í
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
class Solution:
    head = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 参考答案        
        if root is None:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.head
        self.head = root
        return


        # 应该是二叉线索树
        def dfs(root):
            if root is None or(root.left is None and root.right is None):
                return root, root
            right = root.right
            root.right, end = dfs(root.left)
            root.left = None
            if end:
                end.right, new_end = dfs(right)
            else:
                root.right, new_end = dfs(right)
            return root, new_end
        dfs(root)
        return root

        
# @lc code=end

import sys
import json
from typing import List
datas = json.loads(sys.stdin.readline().strip())
# print(datas)
# print(type(datas))
# print(type(datas[0]))
from collections import deque
def build_tree(datas: List[str]) -> Optional[TreeNode]:
    if len(datas) == 0 or datas[0] == None:
        return None
    head = TreeNode(datas[0])
    q = deque([head])
    i = 1
    while i < len(datas):
        cur = q.popleft()
        if i < len(datas) and datas[i] != None:
            cur.left = TreeNode(datas[i])
            q.append(cur.left)
        i += 1
        if i < len(datas) and datas[i] != None:
            cur.right = TreeNode(datas[i])
            q.append(cur.right)
        i += 1
    return head
head = build_tree(datas)
sol = Solution()
sol.flatten(head)


#
# @lcpr case=start
# [1,2,5,3,4,null,6]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


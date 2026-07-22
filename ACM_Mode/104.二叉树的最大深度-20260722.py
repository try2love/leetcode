#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30404
#
# [104] 二叉树的最大深度
# 2:00 核心AC 9:00 ACM AC
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left, right)

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
print(sol.maxDepth(head))

#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=104 lang=python3
# @lcpr version=30400
#
# [104] 二叉树的最大深度
# 4:54 AC 核心模式 14:00 ACM AC
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left, right)
# @lc code=end

import sys
from collections import deque
data = sys.stdin.readline().strip().split()

# 这是大模型给出的标准构建方案
def buildTree(nums):
    if not nums or nums[0]=="null":
        return None
    root = TreeNode(int(nums[0]))
    q = deque([root])
    i = 1
    while q and i< len(nums):
        node = q.popleft()
        if i < len(nums) and nums[i] != "null":
            node.left = TreeNode(int(nums[i]))
            q.append(node.left)
        i+=1
        if i< len(nums) and nums[i] != "null":
            node.right = TreeNode(int(nums[i]))
            q.append(node.right)
        i+=1
    return root

def build_tree(data: List[str]) -> TreeNode:
    if len(data) == 0 or data[0] == "null":
        return None
    root = TreeNode(int(data[0]))
    q = deque([root])
    i = 1
    while i < len(data):
        cur = q.popleft()
        if i < len(data) and data[i] != "null":
            cur.left = TreeNode(int(data[i]))
            q.append(cur.left)
        else:
            cur.left = None
        i += 1
        if i < len(data) and data[i] != "null":
            cur.right = TreeNode(int(data[i]))
            q.append(cur.right)
        else:
            cur.right = None
        i += 1
    return root

root = build_tree(data)
sol = Solution()
ans = sol.maxDepth(root)
print(ans)
#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#


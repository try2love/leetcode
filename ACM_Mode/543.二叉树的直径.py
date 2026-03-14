#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=30400
#
# [543] 二叉树的直径
# 耗时30min，没有写出来答案，也没有写出来数据输入转化为二叉树，需要学习。
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def buildTree(self, nums):
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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        def dfs(node):
            if node is None:
                return -1
            left = dfs(node.left)+1
            right = dfs(node.right)+1
            nonlocal ans
            ans = max(ans, left+right)
            return max(left, right)
        dfs(root)
        return ans

# @lc code=end

import sys
data = sys.stdin.readline().strip().split()
sol = Solution()
# 构建二叉树，输入的data是层序遍历的结果
root = sol.buildTree(data)
ans = sol.diameterOfBinaryTree(root)
print(ans)

#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#


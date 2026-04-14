#
# @lc app=leetcode.cn id=230 lang=python3
# @lcpr version=30403
#
# [230] 二叉搜索树中第 K 小的元素
# 13:10 AC，使用堆排序，我的这个做法适合普通的树，但是这个题是二叉搜索树，中序有序
from typing import Optional
import heapq
from math import inf
# @lc code=start
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Definition for a binary tree node.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # -----参考答案------
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
    
        def dfs(node: Optional[TreeNode]):
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
        # -----参考答案------

        # 思路：遍历，维护一个堆排序
        heap = [-inf]*k
        heapq.heapify(heap)
        def dfs(node:Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            heapq.heappushpop(heap, -node.val)
            dfs(node.right)
        dfs(root)
        return -heap[0]
# @lc code=end



#
# @lcpr case=start
# [3,1,4,null,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,null,1]\n3\n
# @lcpr case=end

#


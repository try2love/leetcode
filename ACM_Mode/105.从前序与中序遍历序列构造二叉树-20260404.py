#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30402
#
# [105] 从前序与中序遍历序列构造二叉树
# 14:47 ACM AC，但是仍然对遍历中序二叉树有疑问，就是如何保证又null，同时最后一层叶子节点的null孩子不输出
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # -----参考答案------
        if not preorder:
            return None
        left_size = inorder.index(preorder[0])
        left = self.buildTree(preorder[1:1+left_size], inorder[:left_size])
        right = self.buildTree(preorder[1+left_size:], inorder[1+left_size:])
        return TreeNode(preorder[0], left, right)
    
        index = {x: i for i,x in enumerate(inorder)}
        def dfs(pre_l:int, pre_r:int, in_l:int):
            if pre_l == pre_r:
                return None
            left_size = index[preorder[pre_l]] - in_l
            left = dfs(pre_l+1, pre_l+1+left_size, in_l)
            right = dfs(pre_l+1+left_size, pre_r, in_l+1+left_size)
            return TreeNode(preorder[pre_l], left, right)
        return dfs(0, len(preorder), 0)
        # -----参考答案------

        if not len(inorder):
            return None
        head = TreeNode(val = preorder[0])
        idx = 0
        while inorder[idx] != preorder[0]:
            idx += 1
        left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        head.left = left
        head.right = right
        return head

# @lc code=end
import sys
import json
from collections import deque
preorder = json.loads(sys.stdin.readline().strip())
inorder = json.loads(sys.stdin.readline().strip())
sol = Solution()
head = sol.buildTree(preorder, inorder)

def print_tree(head: Optional[TreeNode]):
    if head is None:
        print("[null]")
        return
    q = deque([head])
    ans = []
    while q and any(node != None for node in q):
        for _ in range(len(q)):
            cur = q.popleft()
            if cur is None:
                ans.append("null")
                continue
            ans.append(str(cur.val))
            q.append(cur.left)
            q.append(cur.right)
    print(ans)
    return

print_tree(head)
#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#


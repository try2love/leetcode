#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30401
#
# [226] 翻转二叉树
# 耗时太久，20min没A出来，为什么我觉得递归思路没错，但是结果就是错误的呢？
# 到底如何从nums构建二叉树，然后print二叉树？
from typing import Optional
import sys
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # -----参考答案------
        if root is None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
    
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        # -----参考答案------

        # 一眼递归交换左右
        if root is None or (root.left is None and root.right is None):
            return root
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        return root
    
        # -----修改答案------
        # 完全是当局者迷了，root.left = self.invertTree(root.right)，后面在invert left，已经不是之前的left了
        if root is None or (root.left is None and root.right is None):
            return root
        # 所以应该这样，把原始数据都压栈保存
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        # -----修改答案------

    # def print_tree(self, root):
    #     if root is None:
    #         return ["null"]
    #     ans = []
    #     q = deque([root])
    #     while q:
    #         cur = q.pop()
    #         if cur is None:
    #             ans.append("null")
    #             continue
    #         ans.append(cur.val)
    #         if cur.left or root.right:
    #             q.append(cur.left)
    #             q.append(cur.right)
    #     return ans

# @lc code=end

# nums = sys.stdin.readline().strip().split()
# head = TreeNode(val=nums[0])
# dummy = TreeNode(left=head)
# q = deque([head])
# 这个写法最大的错误在于默认输入是一个完全二叉树，实际上并不是。
# def build_tree():
#     pos = 0
#     while pos < len(nums) and q:
#         head = q.pop()
#         if 2*pos+1 < len(nums) and nums[2*pos+1] != "null":
#             head.left = TreeNode(val = int(nums[2*pos + 1]))
#             q.append(head.left)
#         if 2*pos+2 < len(nums) and nums[2*pos+2] != "null":
#             head.right = TreeNode(val = int(nums[2*pos + 2]))
#             q.append(head.right)
#         pos += 1
#     return dummy.left
def build_tree(data_str: str):
    """
    输入格式示例：“[1,2,3,null,null,4,5]”
    """
    if not data_str or data_str == "null":
        return None
    nodes = data_str.replace('[', '').replace(']', '').split(',')
    nodes = [n.strip() for n in nodes]
    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        cur = queue.popleft()
        # 处理左节点
        if i<len(nodes) and nodes[i] != "null":
            cur.left = TreeNode(int(nodes[i]))
            queue.append(cur.left)
        i+=1
        # 处理右节点
        if i<len(nodes) and nodes[i] != "null":
            cur.right = TreeNode(int(nodes[i]))
            queue.append(cur.right)
        i += 1
    return root

def print_tree(root: TreeNode):
    if not root:
        print("[]")
        return
    result = []
    q = deque([root])
    while q:
        layer = len(q)
        for _ in range(layer):
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
    while result and result[-1] == "null":
        result.pop()
    print("[" + ",".join(result) + "]")
nums = input()
root = build_tree(nums)
sol = Solution()
print_tree(root)
root = sol.invertTree(root)
print_tree(root)

#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


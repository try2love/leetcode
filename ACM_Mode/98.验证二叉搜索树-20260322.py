#
# @lc app=leetcode.cn id=98 lang=python3
# @lcpr version=30401
#
# [98] 验证二叉搜索树
# 12:08 ACM AC，使用的是二叉搜索树中序有序的原理，但是忘记了相同元素的处理，所以后面才加入了set
# 能不能尝试使用原生递归？没有头绪啊，如何返回最大最小？
from typing import Optional
from math import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    # 后续遍历用到pre
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode], left=inf, right=inf) -> bool:
        # -----参考答案------
        # 先序遍历
        if root is None:
            return True
        x = root.val
        return left < x < right and \
            self.isValidBST(root.left, left, x) and \
            self.isValidBST(root.right, x, right)

        # 中序遍历
        def dfs(node):
            if node is None:
                return inf, -inf
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            x = node.val
            if x<=l_max or x>=r_min:
                return -inf, inf
            return min(l_min,x), max(r_max,x)
        return dfs(root)[1] != inf
    
        # 后续遍历
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
        # -----参考答案------

        # 中序遍历有序
        # path = []
        # def dfs(root):
        #     if root is None:
        #         return
        #     dfs(root.left)
        #     nonlocal path
        #     path.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return path == sorted(list(set(path)))

        # 左子树找最大，右子树找最小， 下面这个是错误答案
        # if root is None:
        #     return True
        # left = right = True
        # if root.left:
        #     if root.left.val < root.val:
        #         left =  self.isValidBST(root.left)
        #     else:
        #         return False
        # if root.right:
        #     if root.right.val > root.val:
        #         right = self.isValidBST(root.right)
        #     else:
        #         return False
        # return left and right

        # 这里的思想是对的，但是在最后的返回上没有搞对
        # def dfs(root):
        #     if root is None:
        #         return inf, -inf # 最小和最大
            
        #     left_min, left_max = dfs(root.left)
        #     right_min, right_max = dfs(root.right)




# @lc code=end
import sys
from collections import deque
data = sys.stdin.readline().strip().split()
def build_tree(data):
    if len(data) == 0:
        return None
    dummy = TreeNode(left = TreeNode(val = int(data[0])))
    idx = 0
    st = deque([dummy.left])
    while st:
        cur = st.popleft()
        if cur is None:
            continue
        if idx * 2 + 1 >= len(data):
            break
        left = data[idx * 2 + 1]
        if left != "null":
            cur.left = TreeNode(val = int(left))
            st.append(cur.left)
        if idx * 2 + 2 >= len(data):
            break
        right = data[idx * 2 + 2]
        if right != "null":
            cur.right = TreeNode(val = int(right))
            st.append(cur.right)
        idx += 1
    return dummy.left
head = build_tree(data)
sol = Solution()
print(sol.isValidBST(head))

#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,4,null,null,3,6]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30401
#
# [199] 二叉树的右视图
# # 不知道为什么，这个题一直做不对，已经花了40min了
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            ans.append(cur[-1].val)
            nxt = []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            cur = nxt
        return ans

        ans = []
        def dfs(node, depth):
            if node is None:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        dfs(root, 0)
        return ans

        # # 层序遍历每一层的最右侧
        # if not root:
        #     return []
        # st = deque([(root,1)])
        # ans = [root.val]
        # while st:
        #     # 层序+优先右子树
        #     cur, layer = st.popleft()
        #     if cur.left:
        #         st.append((cur.left, layer+1))
        #     if cur.right:
        #         st.append((cur.right, layer + 1))
        #     if layer == len(ans) and st:
        #         ans.append(st[-1][0].val)
        # return ans

# @lc code=end
import sys
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
print(sol.rightSideView(head))

    

#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,null,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#


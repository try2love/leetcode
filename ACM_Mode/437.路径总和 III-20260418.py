#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30403
#
# [437] 路径总和 III
# 38:06 ACM AC
from typing import Optional, List
from collections import Counter, defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # -----参考答案------
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        def dfs(node, s:int): # s表示从根到node到父节点的节点值之和
            if node is None:
                return
            nonlocal ans
            s += node.val
            ans += cnt[s-targetSum]
            cnt[s] += 1
            dfs(node.left, s)
            dfs(node.right, s)
            cnt[s] -= 1
        dfs(root, 0)
        return ans
        # -----参考答案------

        ans = 0
        pre_sum = [0]
        cnt = Counter(pre_sum)
        def dfs(node):
            if not node:
                return
            if cnt[pre_sum[-1] + node.val - targetSum] > 0:                
                nonlocal ans
                ans += cnt[pre_sum[-1] + node.val - targetSum]
            pre_sum.append(pre_sum[-1] + node.val)
            cnt[pre_sum[-1]] += 1
            if node.left:
                dfs(node.left)
                # pre_sum.pop()
            if node.right:
                dfs(node.right)
                # pre_sum.pop()
            cnt[pre_sum[-1]] -= 1
            pre_sum.pop()
        dfs(root)
        return ans

        # 感觉是前缀和
        # 下面这个做法，针对的是不能转弯的问题，实际上这个题可以转弯
        ans = 0
        def dfs(node, left:List[int], right:List[int]):
            nonlocal ans
            if not node:
                return
            left.append(left[-1] + node.val)
            right.append(right[-1] + node.val)
            if left[-1] - targetSum in left:
                ans += 1
            if right[-1] - targetSum in right:
                ans += 1
            if node.left:
                dfs(node.left, left, [0])
            if node.right:
                dfs(node.right, [0], right)
        dfs(root, [0], [0])
        return ans

# @lc code=end
from collections import deque
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
import sys
data_str = sys.stdin.readline().strip()
target = eval(input())
root = build_tree(data_str)
sol = Solution()
print(sol.pathSum(root, target))

#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#


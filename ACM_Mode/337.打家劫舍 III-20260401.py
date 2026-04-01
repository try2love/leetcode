#
# @lc app=leetcode.cn id=337 lang=python3
# @lcpr version=30402
#
# [337] 打家劫舍 III
# 24:39 ACM AC，想了十来分钟终于想起来用两个返回值了。
from typing import Optional, List
from functools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if node is None:
                return 0, 0
            left_use, left_not_use = dfs(node.left)
            right_use, right_not_use = dfs(node.right)
            return node.val + left_not_use+ right_not_use, max(left_use, left_not_use)+max(right_use, right_not_use)
        return max(dfs(root))
        
# @lc code=end
import sys
from collections import deque
data = sys.stdin.readline()

def build_tree(nums: List[str]):
    if nums[0] == "null":
        return None
    q = deque([TreeNode(int(nums[0]))])
    dummy = TreeNode(left=q[0])
    idx = 0
    n = len(nums)
    while q and idx < n:
        for _ in range(len(q)):
            idx += 1
            cur = q.popleft()
            if idx < n:
                cur.left = TreeNode(int(nums[idx])) if nums[idx] != "null" else None
                q.append(cur.left)
            idx += 1
            if idx < n:
                cur.right = TreeNode(int(nums[idx])) if nums[idx] != "null" else None
                q.append(cur.right)
            idx += 1
    return dummy.left

if data == "null":
    print(0)
else:
    sol = Solution()
    root = build_tree(data.strip().split())
    print(sol.rob(root))


#
# @lcpr case=start
# [3,2,3,null,3,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,3,null,1]\n
# @lcpr case=end

#


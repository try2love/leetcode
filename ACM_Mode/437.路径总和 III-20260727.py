#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30404
#
# [437] 路径总和 III
# 9：38，没做出来
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
from collections import Counter, defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 参考答案
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        def dfs(node: Optional[TreeNode], s:int) -> None:
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

        # 感觉是一个二叉前缀和问题
        cnt = Counter()
        ans = 0
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            nonlocal cnt, ans
            # 记录当前节点作为末尾，是否有链路
        
# @lc code=end



#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#


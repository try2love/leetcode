#
# @lc app=leetcode.cn id=108 lang=python3
# @lcpr version=30403
#
# [108] 将有序数组转换为二叉搜索树
# 9:27 ACM AC
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # -----参考答案------
        if not nums:
            return None
        m = len(nums)//2
        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m+1:])
        return TreeNode(nums[m], left, right)
        # -----参考答案------

        if len(nums) == 0:
            return None
        left, right = 0, len(nums)-1
        mid = (left + right) // 2
        return TreeNode(nums[mid], left=self.sortedArrayToBST(nums[left:mid]), right=self.sortedArrayToBST(nums[mid+1:right+1]))

# @lc code=end

import sys
import ast
from collections import deque
nums = ast.literal_eval(sys.stdin.readline().strip())
sol = Solution()
root = sol.sortedArrayToBST(nums)

def print_tree(root):
    ans = []
    if not root:
        return ans
    q = deque([root])
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur:
                ans.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
            else:
                ans.append("null")
    end = len(ans) - 1
    while end >= 0:
        if ans[end] == "null":
            end -= 1
        else:
            break
    print(ans[:end+1])

print_tree(root)


#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#


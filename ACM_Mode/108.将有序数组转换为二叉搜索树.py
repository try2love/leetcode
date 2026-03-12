#
# @lc app=leetcode.cn id=108 lang=python3
# @lcpr version=30400
#
# [108] 将有序数组转换为二叉搜索树
# 总共用时26min，实现核心代码+手动测试用例通过
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 递归构建
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        left, right = 0, len(nums)-1
        middle = (left + right) // 2
        cur = TreeNode(nums[middle])
        cur.left = self.sortedArrayToBST(nums[:middle])
        cur.right = self.sortedArrayToBST(nums[middle+1:])
        return cur
# @lc code=end

from collections import deque
def output_result(cur: TreeNode):
    # 需要层序遍历
    if not cur:
        return []
    ans = []
    st = deque([cur])
    while st:
        node = st.popleft()
        if node is not None:
            ans.append(node.val)
            st.append(node.left)
            st.append(node.right)
        else:
            ans.append(None)
    while ans and ans[-1] is None:
        ans.pop()
    return ans

import sys
data = sys.stdin.readline().strip().split()
data = [int(x) for x in data]
solution = Solution()
result = solution.sortedArrayToBST(data)
print(output_result(result))

#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,3]\n
# @lcpr case=end

#


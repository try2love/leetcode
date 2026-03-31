#
# @lc app=leetcode.cn id=337 lang=python3
# @lcpr version=30402
#
# [337] 打家劫舍 III
# 10分钟，没a出来，错例：[2,1,3,null,4]，输出了6，而不是期望的7
# 还真是，因为我先入为主，认为就是层序遍历，每次选层。实际上上面的示例选3和4.
# 参考答案本质上是后序遍历，先左后右再中间判断
from typing import Optional
from collections import deque
from itertools import cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # -----参考答案------
        def dfs(node):
            if node is None:
                return 0, 0
            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)
            rob = l_not_rob + r_not_rob + node.val
            not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
            return rob, not_rob
        return max(dfs(root))
        # -----参考答案------

        # 父子不能被同时选中
        if root is None:
            return 0
        # 层序遍历
        st = deque()
        st.append(root)
        layer_sum = [] # 每一层的和
        while st:
            layer_sum.append(0)
            for _ in range(len(st)):
                cur = st.popleft()
                layer_sum[-1] += cur.val
                if cur.left:
                    st.append(cur.left)
                if cur.right:
                    st.append(cur.right)
        # 退化为常规的打家劫舍
        @cache
        def dfs(i:int):
            if i<0:
                return 0
            return max(dfs(i-1), dfs(i-2)+layer_sum[i])
        return dfs(len(layer_sum)-1)
                
# @lc code=end



#
# @lcpr case=start
# [3,2,3,null,3,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,3,null,1]\n
# @lcpr case=end

#


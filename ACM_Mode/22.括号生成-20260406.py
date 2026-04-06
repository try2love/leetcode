#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30402
#
# [22] 括号生成
# 8:33 ACM AC
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # -----参考答案------
        ans = []
        path = [''] * (n*2)
        def dfs(left:int, right:int):
            if right == n:
                ans.append("".join(path))
                return
            if left < n:
                path[left + right] = '('
                dfs(left+1, right)
            if right < left:
                path[left + right] = ')'
                dfs(left, right+1)
        dfs(0,0)
        return ans
        # -----参考答案------

        ans = []
        tmp = []
        def dfs(left:int, right:int):
            if left>right or right<=0 or left<0:
                if left==right==0:
                    ans.append("".join(x for x in tmp))
                return
            tmp.append("(")
            dfs(left-1, right)
            tmp.pop()
            tmp.append(")")
            dfs(left, right-1)
            tmp.pop()
        dfs(n, n)
        return ans
        
# @lc code=end
n = eval(input())
sol = Solution()
print(sol.generateParenthesis(n))


#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


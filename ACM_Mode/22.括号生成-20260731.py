#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30404
#
# [22] 括号生成
# 10:45 ACM AC
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        def dfs(i:int ,balance:int) -> None:
            if len(path) == n:
                s = [')'] * (n*2)
                for j in path:
                    s[j] = '('
                ans.append(''.join(s))
                return
            for right in range(balance+1):
                path.append(i+right)
                dfs(i+right+1, balance-right+1)
                path.pop()
        dfs(0, 0)
        return ans
    
        path = ['('] * (2*n)
        # cankao 
        def dfs(left:int, right:int) -> None:
            if right == n:
                ans.append(''.join(path))
                return
            if left < n:
                path[left+right] = '('
                dfs(left+1, right)
            if right < left:
                path[left+right] = ')'
                dfs(left, right+1)
        dfs(0, 0)
        return ans

        def dfs(i:int, left:int, right:int):
            if left == right == 0:
                ans.append(''.join(path))
                return
            if right < left or left<0 or right<0 or i>=(2*n):
                return
            # 当前第i个位置，可以选left可以选right
            path[i] = '('
            dfs(i+1, left-1, right)
            path[i] = ')'
            dfs(i+1, left, right-1)
        dfs(0, n, n)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#


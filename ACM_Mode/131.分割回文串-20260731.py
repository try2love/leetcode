#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30404
#
# [131] 分割回文串
# 14:09 错误case： efe，没有返回本体 16:57 ACM AC，因为判断条件多写了，提前返回了
from typing import List
# @lc code=start
class Solution:
    def isHuiwen(self, s:str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []
        # 参考答案
        def dfs(i:int):
            if i == n:
                ans.append(path[:])
                return
            for j in range(i, n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans

        def dfs(i:int, start:int) -> None:
            if i == n:
                ans.append(path[:])
                return
            if i < n-1:
                dfs(i+1, start)
            t = s[start: i+1]
            if t == t[::-1]:
                path.append(t)
                dfs(i+1, i+1)
                path.pop()
        dfs(0, 0)
        return ans
    
        # 是否以i作为结尾
        def dfs(i:int, s:str):
            if len(s) == 0:
                ans.append(path[:])
                return
            if i>=len(s):
                return
            # 以i作为结尾
            if self.isHuiwen(s[:i+1]):
                path.append(s[:i+1])
                dfs(0, s[i+1:])
                path.pop()
            dfs(i+1, s)
        dfs(0, s)
        return ans

# @lc code=end

s = input()
sol = Solution()
print(sol.partition(s))
#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#


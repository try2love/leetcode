#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30401
#
# [131] 分割回文串
# 花费13；30，完全没有头绪
from typing import List
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # -----参考答案------
        n = len(s)
        ans = []
        path = []
        # 方法1:枚举逗号分隔符的位置
        def dfs(i:int, start:int):
            # 考虑i后面的逗号怎么选；start表示当前回文子串的开始位置
            if i == n:
                ans.append(path.copy())
                return
            # 部分歌，选择i和i+1之间的逗号
            if i < n-1:
                dfs(i+1, start)
            t = s[start: i+1]
            if t==t[::-1]:
                path.append(t)
                dfs(i+1, i+1)
                path.pop()
        dfs(0,0)
        return ans
    
        # 方法2:从答案的视角
        def dfs(i:int):
            if i==n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
            dfs(0)
            return ans
        # -----参考答案------

        # ans = [list(s)]
        # # 表示从row到col之间为回文串
        # dp = [[False]*len(s) for _ in range(len(s))]
        # for i, ch in enumerate(s):
        #     dp[i][i] = True
        #     for j in range(i+1,len(s)):

        
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


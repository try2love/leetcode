#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30403
#
# [79] 单词搜索
# 13:58 ACM AC
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        # -----参考答案------
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word): # 第一个优化点：提前剪枝
            return False
        if cnt[word[-1]] < cnt[word[0]]: # 优化二
            word = word[::-1]
        def dfs(i:int, j:int, k:int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1:
                return True
            board[i][j] = "" # 标记为访问过的
            for x,y in (i, j-1), (i, j+1), (i-1,j), (i+1, j):
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k+1):
                    return True
            board[i][j] = word[k]
            return False
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))

        def dfs(i:int, j:int, k:int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = '' # 标记访问过
            for x, y in (i, j-1), (i, j+1), (i-1,j), (i+1, j):
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k+1):
                    return True
            board[i][j] = word[k]
            return False
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
        # -----参考答案------

        visited = [[0]*n for _ in range(m)]
        def dfs(i:int, j:int, length:int):
            if length == len(word):
                return True
            if i<0 or j<0 or i>=m or j>=n or visited[i][j] or board[i][j] != word[length]:
                return False
            visited[i][j] = 1
            res = any([dfs(i+1,j,length+1),dfs(i-1,j,length+1),dfs(i,j+1,length+1),dfs(i,j-1,length+1)])
            visited[i][j] = 0
            return res
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == word[0]:
                    ans = dfs(i,j,0)
                    if ans:
                        return True
        return False

# @lc code=end
import sys
import json
# json.loads无法识别单引号[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
# board = json.loads(sys.stdin.readline().strip())
board = json.loads(sys.stdin.readline().strip().replace("'", '"'))

# import ast
# # 直接替换你的 json.loads
# line = sys.stdin.readline().strip()
# if line:
#     board = ast.literal_eval(line)

word = sys.stdin.readline().strip()
sol = Solution()
print(sol.exist(board, word))


#
# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
# @lcpr case=end

#


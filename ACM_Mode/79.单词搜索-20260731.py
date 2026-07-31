#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30404
#
# [79] 单词搜索
# 12:39 ACM AC
from typing import List
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        # cankao
        from collections import Counter
        cnt = Counter(c for row in board for c in row)
        if not cnt>=Counter(word):
            return False
        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]
        
        def dfs(i:int,j:int,k:int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k==len(word)-1:
                return True
            board[i][j] = ''
            for x, y in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0<=x<m and 0<=y<n and dfs(x,y,k+1):
                    return True
            board[i][j] = word[k]
            return False
        return any(dfs(i,j,0) for i in range(m) for j in range(n))

        visited = [[False]* n for _ in range(m)]
        def dfs(i:int, row:int, col:int):
            if i>=len(word):
                return True
            if row < 0 or col<0 or row>=m or col>=n or word[i]!=board[row][col] or visited[row][col] == True:
                return False
            visited[row][col] = True
            a = dfs(i+1, row+1, col)
            b = dfs(i+1, row-1, col)
            c = dfs(i+1, row, col+1)
            d = dfs(i+1, row, col-1)
            visited[row][col] = False
            return any([a,b,c,d])
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == word[0] and dfs(0, i, j):
                    return True
        return False
        
# @lc code=end



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


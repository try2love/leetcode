#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30404
#
# [17] 电话号码的字母组合
# 6:17 ACM AC
from typing import List
# @lc code=start
MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"

alphabat = {"2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
            }
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 参考答案
        n = len(digits)
        if n==0:
            return []
        ans = []
        path = [''] * n
        def dfs(i:int) -> None:
            if i == n:
                ans.append(''.join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs(0)
        return ans

        ans = []
        path = ['a'] * len(digits)
        def dfs(i: int):
            if i == len(digits):
                ans.append("".join(path))
                return
            for x in alphabat[digits[i]]:
                path[i] = x
                dfs(i+1)
        dfs(0)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#


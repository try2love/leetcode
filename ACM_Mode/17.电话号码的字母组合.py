#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30400
#
# [17] 电话号码的字母组合
# 10min46s核心模式 11min40sACM模式
from typing import List

# @lc code=start
alphabat = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(digits)
        digits = [int(x) for x in digits]
        n = len(digits)
        ans = []
        tmp = ["a"] * n
        def dfs(i:int, tmp:List[str]):
            if i >= n:
                ans.append("".join(tmp[:]))
                return
            cur = digits[i] # 当前的数字
            for x in alphabat[cur]:
                tmp[i] = x
                dfs(i+1, tmp)
        dfs(0, tmp)
        return ans

# @lc code=end

import sys
data = sys.stdin.read().strip().split() # list
# print(data, type(data))
data = str(data[0])
sol = Solution()
ans = sol.letterCombinations(data)
print(ans)

#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=28 lang=python3
# @lcpr version=30404
#
# [28] 找出字符串中第一个匹配项的下标
# 6:40 ACM AC

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        flag = False
        for i in range(m-n+1):
            if needle[0] != haystack[i]:
                continue
            for j in range(n):
                if needle[j] == haystack[i+j]:
                    if j==n-1:
                        flag=True
                    continue
                else:
                    break
            if flag:
                return i
        return -1


        
# @lc code=end



#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#


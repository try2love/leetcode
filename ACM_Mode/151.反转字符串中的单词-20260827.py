#
# @lc app=leetcode.cn id=151 lang=python3
# @lcpr version=30404
#
# [151] 反转字符串中的单词
# 1:07 ACM AC

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
# @lc code=end



#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

#


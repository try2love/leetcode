#
# @lc app=leetcode.cn id=58 lang=python3
# @lcpr version=30404
#
# [58] 最后一个单词的长度
# 0:53 ACM AC

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
# @lc code=end



#
# @lcpr case=start
# "Hello World"\n
# @lcpr case=end

# @lcpr case=start
# "   fly me   to   the moon  "\n
# @lcpr case=end

# @lcpr case=start
# "luffy is still joyboy"\n
# @lcpr case=end

#


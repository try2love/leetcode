#
# @lc app=leetcode.cn id=383 lang=python3
# @lcpr version=30404
#
# [383] 赎金信
# 1:18 ACM AC
from collections import Counter
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(magazine) >= Counter(ransomNote)

# @lc code=end



#
# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aab"\n
# @lcpr case=end

#


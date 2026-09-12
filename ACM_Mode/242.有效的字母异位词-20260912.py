#
# @lc app=leetcode.cn id=242 lang=python3
# @lcpr version=30404
#
# [242] 有效的字母异位词
# 1:17 ACM AC
from collections import Counter
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(t) == Counter(s)
        
# @lc code=end



#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#


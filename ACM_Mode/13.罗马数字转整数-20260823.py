#
# @lc app=leetcode.cn id=13 lang=python3
# @lcpr version=30404
#
# [13] 罗马数字转整数
# 3:33 ACM AC

# @lc code=start
rome = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        pre = None
        for ch in s[::-1]:
            if pre and rome[pre] > rome[ch]:
                ans -= rome[ch]
            else:
                ans += rome[ch]
            pre = ch
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "III"\n
# @lcpr case=end

# @lcpr case=start
# "LVIII"\n
# @lcpr case=end

# @lcpr case=start
# "MCMXCIV"\n
# @lcpr case=end

#


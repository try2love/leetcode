#
# @lc app=leetcode.cn id=12 lang=python3
# @lcpr version=30404
#
# [12] 整数转罗马数字
# 12:40 ACM aC

# @lc code=start
rome = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        for idx, ch in enumerate(str(num)[::-1]):
            x = int(ch)
            if 0< x <= 3:
                ans += rome[10**idx] * x
            elif x == 4:
                ans += rome[5*(10**idx)]
                ans += rome[10**idx]
            elif x == 5:
                ans += rome[5*(10**idx)]
            elif x == 9:
                ans += rome[10**(idx+1)]
                ans += rome[10**idx]
            elif 5 < x < 9:
                left = x-5
                ans += rome[10**idx] * left
                ans += rome[5*(10**idx)]
        return ans[::-1]
# @lc code=end



#
# @lcpr case=start
# 3749\n
# @lcpr case=end

# @lcpr case=start
# 58\n
# @lcpr case=end

# @lcpr case=start
# 1994\n
# @lcpr case=end

#


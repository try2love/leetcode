#
# @lc app=leetcode.cn id=125 lang=python3
# @lcpr version=30404
#
# [125] 验证回文串
# 3:16 ACM AC

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 参考答案
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

        i, j = 0, len(s) - 1
        while i<j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

        cur = ""
        for ch in s.lower():
            if ord('a') <= ord(ch) <= ord('z') or ord('0') <= ord(ch) <= ord('9'):
                cur += ch
        return cur == cur[::-1]
# @lc code=end



#
# @lcpr case=start
# "A man, a plan, a canal: Panama"\n
# @lcpr case=end

# @lcpr case=start
# "race a car"\n
# @lcpr case=end

# @lcpr case=start
# " "\n
# @lcpr case=end

#


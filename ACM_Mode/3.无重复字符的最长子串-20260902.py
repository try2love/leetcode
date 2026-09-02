#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30404
#
# [3] 无重复字符的最长子串
# 6:01 ACM AC
from collections import defaultdict
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 参考答案
        ans = left = 0
        window = set()
        for right, c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left += 1
            window.add(c)
            ans = max(ans, right-left+1)
        return ans

        if len(s) <= 1:
            return len(s)
        left = 0
        cnt = defaultdict(int)
        ans = 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch]>1 and left <= right:
                left += 1
                cnt[s[left-1]] -= 1
            ans = max(ans, right-left+1)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#


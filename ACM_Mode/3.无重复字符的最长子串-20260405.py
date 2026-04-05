#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30402
#
# [3] 无重复字符的最长子串
# 9:00 ACM AC
from collections import defaultdict
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # -----参考答案------
        ans = left = 0
        cnt = defaultdict(int)
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans

        ans = left = 0
        window = set()
        for right, c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left += 1
            window.add(c)
            ans = max(ans, right-left+1)
        return ans
        # -----参考答案------

        # 滑动窗口
        if len(s) == 0:
            return 0
        # 左闭右开
        left = 0
        right = 1
        cnt = defaultdict(int)
        cnt[s[0]] = 1
        ans = 1
        while right < len(s):
            while cnt[s[right]] > 0:
                cnt[s[left]] -= 1
                left += 1
            cnt[s[right]] += 1
            right += 1
            ans = max(right-left, ans)
        return ans

# @lc code=end
s = input()
sol = Solution()
print(sol.lengthOfLongestSubstring(s))


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


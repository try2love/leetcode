#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30404
#
# [438] 找到字符串中所有字母异位词
# 10:04 ACM AC
from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 变长
        cnt = Counter(p)
        ans = []
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                ans.append(left)
        return ans
        
        # 定长
        cnt_p = Counter(p)
        cnt_s = Counter()
        ans = []
        for right, c in enumerate(s):
            cnt_s[c] += 1
            left = right - len(p) + 1
            if left < 0:
                continue
            if cnt_s == cnt_p:
                ans.append(left)
            cnt_s[s[left]] -= 1
        return ans
        
        # 滑动窗口
        ans = []
        target = Counter(p)
        left = 0
        right = len(p) - 1
        window = Counter(s[left:right])
        while right < len(s):
            window[s[right]] += 1
            if window == target:
                ans.append(left)
            window[s[left]] -= 1
            left += 1
            right += 1
        return ans

# @lc code=end
s = input()
p = input()
sol = Solution()
print(sol.findAnagrams(s, p))

#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#


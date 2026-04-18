#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30403
#
# [438] 找到字符串中所有字母异位词
# 12:23 ACM AC
from typing import List
from collections import Counter, defaultdict
# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # -----参考答案------
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
        # -----参考答案------

        # 哈希表+滑动窗口
        cnt = Counter(p)
        cnt_s = Counter(s)
        if cnt_s < cnt or len(s) < len(p):
            return []
        hash_map = Counter()
        for i in range(len(p)-1):
            hash_map[s[i]] += 1
        ans = []
        for end in range(len(p)-1, len(s)):
            start = end - len(p)+1
            hash_map[s[end]] += 1
            if hash_map == cnt:
                ans.append(start)
            hash_map[s[start]] -= 1
        if hash_map == cnt:
            ans.append(start)
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


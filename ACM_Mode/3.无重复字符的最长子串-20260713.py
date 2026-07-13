#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30404
#
# [3] 无重复字符的最长子串
# 9:54 ACM AC
from collections import defaultdict
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希表：布尔型
        ans = left = 0
        window = set()
        for right, c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left += 1
            window.add(c)
            ans = max(ans, right-left+1)
        return ans
        
        # 哈希表：整型数组
        ans = left = 0
        cnt = defaultdict(int)
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans
        
        # 双指针+哈希表，虫子蠕动法
        ans = 0
        cnt = set([])
        left = right = 0
        while right < len(s):
            if s[right] not in cnt:
                cnt.add(s[right])
                right += 1
            else:
                ans = max(ans, right - left)
                cnt.remove(s[left])
                left += 1
        ans = max(ans, right-left)
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


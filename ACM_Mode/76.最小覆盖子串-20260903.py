#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30404
#
# [76] 最小覆盖子串
# 9:03 ACM AC
from collections import Counter, defaultdict
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 参考答案
        diff = defaultdict(int)
        for c in t:
            diff[c] -= 1
        kinds = len(diff)
        ans_left, ans_right = -1, len(s)
        ge_cnt = 0
        left = 0
        for right, c in enumerate(s):
            diff[c] += 1
            if diff[c] == 0:
                ge_cnt += 1
            while ge_cnt == kinds:
                if right - left < ans_right-ans_left:
                    ans_left, ans_right = left, right
                x = s[left]
                if diff[x] == 0:
                    ge_cnt -= 1
                diff[x] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right+1]

        cnt_s = Counter()
        cnt_t = Counter(t)
        ans_left, ans_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:
                if right-left < ans_right-ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right+1]

        target = Counter(t)
        if not Counter(s) >= target:
            return ""
        ans = s
        cnt = Counter([])
        left = 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            while cnt >= target:
                ans = s[left:right+1] if len(ans)>right-left+1 else ans
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    del cnt[s[left]]
                left += 1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#


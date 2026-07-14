#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30404
#
# [76] 最小覆盖子串
# 13:06 ACM AC
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
                if right-left < ans_right-ans_left:
                    ans_left, ans_right = left, right
                x = s[left]
                if diff[x] == 0:
                    ge_cnt -= 1
                diff[x] -= 1
                left += 1
        return "" if ans_left<0 else s[ans_left: ans_right+1]
        
        cnt_s = Counter()
        cnt_t = Counter(t)
        ans_left, ans_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:
                if right-left < ans_right-ans_left:
                    ans_left = left
                    ans_right = right
                cnt_s[s[left]] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left:ans_right+1]
        
        # 蠕动窗口+哈希表
        if len(t) == 0 or len(s) < len(t):
            return ""
        target = Counter(t)
        valid = Counter(s)
        for k in target:
            if k not in valid or target[k] > valid[k]:
                return ""
        if len(t) == 1 and t in valid:
            return t
        del valid
        window = Counter()
        ans = s
        left = 0
        while s[left] not in target:
            left += 1
        right = left + 1 # 左闭右开
        window[s[left]] += 1
        while right < len(s):
            window[s[right]] += 1
            while window >= target:
                ans = s[left:right+1] if right-left+1 < len(ans) else ans
                if len(ans) == len(t):
                    return ans
                window[s[left]] -= 1
                left += 1
            right += 1
        return ans

# @lc code=end

s = input()
t = input()
sol = Solution()
print(sol.minWindow(s, t))


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


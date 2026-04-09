#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30403
#
# [76] 最小覆盖子串
# 23:51,通过243/268 看答案
from math import inf
from collections import defaultdict, Counter
# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # -----参考答案------
        cnt_s = Counter()
        cnt_t = Counter(t)
        ans_left, ans_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                left += 1
        return "" if ans_left < 0 else s[ans_left:ans_right+1]

        diff = defaultdict(int)
        for c in t:
            diff[c] -= 1
        kinds = len(diff) # t中有kinds种不同的字母
        ans_left, ans_right = -1, len(s)
        ge_cnt = 0 # 窗口内有ge_cnt种字母出现的次数>=t中相应字母的出现次数
        left = 0
        for right, c in enumerate(s): # 移动子串右端点
            diff[c] += 1 # 右端点字母移入子串
            if diff[c] == 0: # 原来窗口内c的出现次数比t的少，现在一样多
                ge_cnt += 1 # 从< 变成 >=
            while ge_cnt == kinds: # 涵盖：所有的字母出现次数都是>=
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                x = s[left] # 左端点字母
                if diff[x] == 0:
                    # x移出窗口之前，检查出现次数
                    # 如果窗口内x的出现次数和t一样
                    # 那么x移出窗口后，窗口内x的出现次数比t的少
                    ge_cnt -= 1 # 从>=变为<
                diff[x] -= 1 # 左端点移出
                left += 1
        return "" if ans_left < 0 else s[ans_left:ans_right+1]

        # -----参考答案------

        m, n = len(s), len(t)
        # 双指针
        ans = ""
        left = 0
        right = 1 # 左闭右开
        length = inf
        cnt_t = Counter(t)
        cnt_win = Counter()
        while left < m and right <=m:
            while right <= m:
                if s[right-1] in cnt_t:
                    cnt_win[s[right-1]] += 1
                right += 1
                if cnt_win >= cnt_t:
                    break
            if cnt_win >= cnt_t and length > right-left:
                length = right - left
                ans = s[left:right-1]
            while left < right:
                if s[left] in cnt_t:
                    cnt_win[s[left]] -= 1
                left += 1
                if cnt_win >= cnt_t and length > right-left:
                    length = right - left
                    ans = s[left:right-1]
                elif cnt_win < cnt_t:
                    break
        return ans


# @lc code=end

s = input().strip()
t = input().strip()
sol = Solution()
print(sol.minWindow(s,t))

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


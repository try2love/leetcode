#
# @lc app=leetcode.cn id=392 lang=python3
# @lcpr version=30404
#
# [392] 判断子序列
# 4:01 ACM AC

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 参考答案
        # 进阶
        n = len(t)
        nxt = [[n]*26 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            nxt[i][:] = nxt[i+1]
            nxt[i][ord(t[i]) - ord('a')] = i
        i = -1
        for c in s:
            i = nxt[i+1][ord(c) - ord('a')]
            if i == n:
                return False
        return True

        it = iter(t)
        return all(c in it for c in s)

        if not s:
            return True
        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                if i == len(s):
                    return True
        return False

        m, n = len(s), len(t)
        j = 0
        for i in range(m):
            while j < n and s[i] != t[j]:
                j += 1
            if j >= n:
                return False
            i += 1
            j += 1
        return True
# @lc code=end



#
# @lcpr case=start
# "abc"\n"ahbgdc"\n
# @lcpr case=end

# @lcpr case=start
# "axc"\n"ahbgdc"\n
# @lcpr case=end

#


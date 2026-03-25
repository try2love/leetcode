#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30401
#
# [5] 最长回文子串
# 花了十分钟，只能想起来分奇偶情况，但是一点都没写出来

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # -----参考答案------
        n = len(s)
        ans_left = ans_right = 0 # 维护左闭右开区间，因为返回字符串是左闭右开
        # 奇回文串
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > ans_right - ans_left:
                ans_left, ans_right = l+1, r

        # 偶回文串
        for i in range(n-1):
            l, r = i, i+1
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l+1, r
        return s[ans_left:ans_right]
    
        # 方案2:奇偶合并
        n = len(s)
        ans_left = ans_right = 0
        for i in range(2*n-1):
            l, r = i//2, (i+1)//2
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            if r-l-1>ans_right - ans_left:
                ans_left, ans_right = l+1, r
        return s[ans_left:ans_right]
        # -----参考答案------

        # def dfs(i:int, j:int):
        #     if i > j:
        #         return ""
        #     if s[i] != s[j]:
        #         return dfs(i+1,j), dfs(i,j-1), dfs(i+1,j-1)
        #     else:
        #         return s[i] + dfs(i+1, j-1) + s[j]
        # 应该要考虑奇数的回文和偶数的回文
        # start = 0
        # end = start + 1
        # while end < len(s) and s[start] != s[end]:
        #     start += 1
        #     end += 1
        # if end >= len(s)

# @lc code=end

s = input()
sol = Solution()
print(sol.longestPalindrome(s))

#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#


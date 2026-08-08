#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30404
#
# [5] 最长回文子串
# 14:23 超市

# @lc code=start
class Solution:
    def isHui(self, s:str) -> bool:
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        # 参考答案
        n = len(s)
        ans_left = ans_right = 0
        for i in range(2*n-1):
            l, r = i//2, (i+1)//2
            while l>=0 and r<n and s[l]==s[r]:
                l -= 1
                r += 1
            if r-l-1 > ans_right-ans_left:
                ans_left, ans_right = l+1, r
        return s[ans_left: ans_right]

        n = len(s)
        ans_left = ans_right = 0

        # 奇回文串
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            # 循环结束后，s[l+1] 到 s[r-1] 是回文串
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开区间

        # 偶回文串
        for i in range(n - 1):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > ans_right - ans_left:
                ans_left, ans_right = l + 1, r  # 左闭右开区间

        return s[ans_left: ans_right]

        # 我记得这个题要区分奇数和偶数
        ans = s[0]
        left = right = 0
        for mid,x in enumerate(s):
            # 奇数，以mid为中间，向两边扩散
            left = right = mid
            left -= 1
            right += 1
            while left >=0 and right < len(s):
                if self.isHui(s[left:right+1]) and right-left+1>len(ans):
                    ans = s[left:right+1]
                elif not self.isHui(s[left:right+1]):
                    break
                left -= 1
                right += 1
        # 找偶数
        a = 0
        b = 1
        while b<len(s):
            if s[a] == s[b]:
                if len(ans)==1:
                    ans = s[a:b+1]
                # 扩散
                left=a
                right=b
                left -= 1
                right += 1
                while left >=0 and right < len(s):
                    if self.isHui(s[left:right+1]) and right-left+1>len(ans):
                        ans = s[left:right+1]
                    elif not self.isHui(s[left:right+1]):
                        break
                    left -= 1
                    right += 1
            a += 1
            b += 1
        return ans
                    
        
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


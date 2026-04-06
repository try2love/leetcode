#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30402
#
# [20] 有效的括号
# 6:00 ACM AC

# @lc code=start
class Solution:
    judge = {")": "(", "]": "[", "}": "{"}
    def isValid(self, s: str) -> bool:
        st = [] # 用list模拟栈
        for x in s:
            if x in self.judge.values():
                st.append(x)
            else:
                if len(st)==0 or st.pop() != self.judge[x]:
                    return False
        return len(st) == 0
                

# @lc code=end
s = input()
sol = Solution()
print(sol.isValid(s))


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#


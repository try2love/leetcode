#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30404
#
# [20] 有效的括号
# 4：57 ACM AC

# @lc code=start
hash_map = {']': '[',
            ')': '(',
            '}': '{'}
class Solution:
    def isValid(self, s: str) -> bool:
        # 一眼栈
        if len(s)%2==1 or s[0] in [')', ']', '}']:
            return False
        st = []
        for ch in s:
            if ch in ['(', '[', '{']:
                st.append(ch)
            else:
                if len(st)==0 or st.pop() != hash_map[ch]:
                    return False
        return len(st)==0
        
# @lc code=end



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


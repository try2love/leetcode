#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30404
#
# [20] 有效的括号
# 4:03 ACM AC

# @lc code=start
hash_map = {')':"(", ']':'[', '}':'{'}
class Solution:
    def isValid(self, s: str) -> bool:
        # 参考
        if len(s)%2:
            return False
        mp = {'(': ')', '[': ']', '{': '}'}
        st = []
        for c in s:
            if c in mp:
                st.append(mp[c])
            elif not st or st.pop() != c:
                return False
        return not st
    
        st = []
        for c in s:
            if c not in hash_map:
                st.append(c)
            elif not st or st.pop() != hash_map[c]:
                return False
        return not st

        if len(s) % 2 != 0:
            return False
        st = []
        for ch in s:
            if ch in ["(", '[', '{']:
                st.append(ch)
            else:
                if len(st)==0 or hash_map[ch] != st.pop():
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


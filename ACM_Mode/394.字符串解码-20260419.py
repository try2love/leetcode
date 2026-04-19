#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30403
#
# [394] 字符串解码
# 19:38 ACM AC，但是时间太高了，因为把每一个字母拆分后填回去
# 修改为对字符串最后一个的判断，直接大幅度提高效率
from collections import deque
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        # -----参考答案------
        st = []
        res = ''
        k = 0
        for c in s:
            if c.isalpha():
                res += c
            elif c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                st.append((res, k))
                res = ''
                k = 0
            else:
                pre_res, pre_k = st.pop()
                res = pre_res + res * pre_k
        return res

        i = 0
        def decode() -> str:
            nonlocal i
            res = ''
            k = 0
            while i < len(s):
                c = s[i]
                i += 1
                if c.isalpha():
                    res += c
                elif c.isdigit():
                    k = k * 10 + int(c)
                elif c == "[":
                    res += decode() * k
                    k = 0
                else:
                    break
            return res
        return decode()
        # -----参考答案------

        # 用栈
        if not s:
            return ""
        alphabat = [chr(idx) for idx in range(ord('a'), ord('z')+1)]
        alphabat.extend("[")
        q = deque()
        ans = ""
        for x in s:
            if x != "]":
                q.append(x)
                continue
            tmp = ""
            times = ""
            tmp = q.pop() + tmp
            # while q:
            while q[-1] != "[":
                tmp = q.pop() + tmp
            q.pop() # 弹出[
            while q and q[-1][-1] not in alphabat:
                times = q.pop() + times
            times = int(times)
            if not q:
                ans += tmp * times
            else:
                # q.extend([ch for ch in tmp*times])
                q.append(tmp*times)
        return ans + "".join(x for x in q)

# @lc code=end

s = input()
sol = Solution()
print(sol.decodeString(s))

#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

#


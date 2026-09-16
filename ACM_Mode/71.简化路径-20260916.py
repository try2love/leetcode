#
# @lc app=leetcode.cn id=71 lang=python3
# @lcpr version=30404
#
# [71] 简化路径
# 12:18 ACM AC

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # 参考答案
        stk = []
        for s in path.split('/'):
            if s == "" or s == ".":
                continue
            if s != "..":
                stk.append(s)
            elif stk:
                stk.pop()
        return '/'+'/'.join(stk)

        paths = path.split('/')
        ans = []
        for p in paths:
            if p == '':
                continue
            if p == '..':
                if len(ans)!=0:
                    ans.pop()
            elif p == '.':
                continue
            else:
                ans.append(p)
        print(ans)
        return '/'+'/'.join(ans)
        
# @lc code=end

path = "/home//foo/"
sol = Solution()
print(sol.simplifyPath(path))

#
# @lcpr case=start
# "/home/"\n
# @lcpr case=end

# @lcpr case=start
# "/home//foo/"\n
# @lcpr case=end

# @lcpr case=start
# "/home/user/Documents/../Pictures"\n
# @lcpr case=end

# @lcpr case=start
# "/../"\n
# @lcpr case=end

# @lcpr case=start
# "/.../a/../b/c/../d/./"\n
# @lcpr case=end

#


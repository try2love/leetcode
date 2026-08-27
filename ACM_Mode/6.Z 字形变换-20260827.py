#
# @lc app=leetcode.cn id=6 lang=python3
# @lcpr version=30404
#
# [6] Z 字形变换
# 7:47 放弃

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 只感觉和数学相关，没具体推导出来
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows-1:
                flag = -flag
            i += flag
        return "".join(res)

# @lc code=end



#
# @lcpr case=start
# "PAYPALISHIRING"\n3\n
# @lcpr case=end

# @lcpr case=start
# "PAYPALISHIRING"\n4\n
# @lcpr case=end

# @lcpr case=start
# "A"\n1\n
# @lcpr case=end

#


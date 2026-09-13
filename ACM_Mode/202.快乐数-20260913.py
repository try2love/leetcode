#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30404
#
# [202] 快乐数
# 4:12 隐约感觉到要用递归

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # 参考答案
        seen = {1}
        while n not in seen:
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n==1

        if n == 1 or (n!=0 and n%10==0):
            return True

        
# @lc code=end



#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#


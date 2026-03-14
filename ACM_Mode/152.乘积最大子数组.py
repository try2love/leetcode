#
# @lc app=leetcode.cn id=152 lang=python3
# @lcpr version=30400
#
# [152] 乘积最大子数组
# 20min40s完成全部的实现，最搞的是函数里面对0判断之后应该要break的，要不然又要走一轮了，这个点多亏了vscode的debug
# 看了灵神的答案，发现最后完全没必要对0单独判断，因为我们已经在min和max中加入了x，遇见0也没事。
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ans = cur_max = cur_min = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            if x>0:
                cur_max = max(cur_max*x, x)
                cur_min = min(cur_min*x, x)
                ans = max(cur_max, ans)
            else:
                cur_max, cur_min = max(cur_min*x, x), min(cur_max*x, x)
                ans = max(cur_max, ans)
            # elif x < 0:
            #     cur_max, cur_min = max(cur_min*x, x), min(cur_max*x, x)
            #     ans = max(cur_max, ans)
            # else: # x==0
            #     ans = max(ans, cur_max, cur_min, 0, self.maxProduct(nums[i+1:]))
            #     break
        return ans
# @lc code=end
# import sys
# data = sys.stdin.readline().strip().split()
data = input()
print(data, type(data))
data = data.strip().split()
print(data, type(data))
data = [int(x) for x in data]
sol = Solution()
ans = sol.maxProduct(data)
print(ans)

#
# @lcpr case=start
# [2,3,-2,4]\n
# @lcpr case=end

# @lcpr case=start
# [-2,0,-1]\n
# @lcpr case=end

#


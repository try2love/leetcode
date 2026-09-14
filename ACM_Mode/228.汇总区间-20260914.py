#
# @lc app=leetcode.cn id=228 lang=python3
# @lcpr version=30404
#
# [228] 汇总区间
# 8:32 ACM AC
from typing import List
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 参考答案
        def f(i:int, j:int) -> str:
            return str(nums[i]) if i==j else f'{nums[i]}->{nums[j]}'
        i = 0
        n = len(nums)
        ans = []
        while i<n:
            j = i
            while j+1 < n and nums[j+1] == nums[j] + 1:
                j += 1
            ans.append(f(i,j))
            i = j+1
        return ans

        end = 0
        ans = []
        for i,x in enumerate(nums):
            if i == end:
                ans.append(str(x))
                continue
            if x != nums[i-1]+1:
                ans[-1] = ans[-1]+"->"+str(nums[end]) if ans[-1] != str(nums[end]) else ans[-1]
                ans.append(str(x))
            end += 1
            if i == len(nums)-1 and ans[-1] != str(nums[-1]):
                ans[-1] = ans[-1] + "->" + str(nums[-1])
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [0,1,2,4,5,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,2,3,4,6,8,9]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30400
#
# [560] 和为 K 的子数组
# 元素有正有负，难道要用回溯？尝试一下双指针吧
# 不单调，还要连续，考虑使用前缀和
# 没有提示A出来核心耗时大概28min，加上输入输出总共耗时 35min左右
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        ans = 0
        total = nums[0]
        cnt = defaultdict(int)
        cnt[total] += 1
        ans += cnt[k]
        for i in range(1,len(nums)):
            total += nums[i]
            if total == k:
                ans += 1
            if total-k in cnt:
                ans += cnt[total-k]
            cnt[total] += 1
        return ans

# @lc code=end
import sys
data = sys.stdin.readlines()
nums = data[0].strip().split()
nums = [int(x) for x in nums]
k = int(data[1])
solution = Solution()
print(solution.subarraySum(nums, k))


#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#


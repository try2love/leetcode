#
# @lc app=leetcode.cn id=2560 lang=python3
# @lcpr version=30402
#
# [2560] 打家劫舍 IV
# 20:50 没有AC，最开始排查问题，发现加了记忆化导致回溯错误。
# 修改后超时，看看答案如何剪枝吧
from typing import List
from functools import cache
from math import inf
from bisect import bisect_left
# @lc code=start
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # -----参考答案------
        # 方法1:二分+dp
        # 看到「最大化最小值」或者「最小化最大值」就要想到二分答案，这是一个固定的套路。
        # 返回最大金额为mx时，最多可以偷多少房子
        def solve(mx:int):
            f0 = f1 = 0
            for x in nums:
                if x > mx: # 当前价值超过上限，不能偷
                    f0 = f1
                else:
                    f0, f1 = f1, max(f1, f0+1) # 这里是+1，强调的是数量
            return f1
        return bisect_left(range(max(nums)), k, key = solve)
        # 搜索范围：range(max(nums))。能力值最小是 0（虽然不可能），最大不会超过数组中的最大值。
        # 判断准则：key=solve。二分查找会自动调用 solve(mid)。
        # 目标：寻找第一个使得 solve(mid) >= k 的 mid 值。
    
        # 方法2:二分+贪心
        def solve(mx:int):
            cnt = i = 0
            while i < len(nums):
                if nums[i] > mx:
                    i += 1
                else:
                    cnt += 1
                    i += 2
            return cnt
        return bisect_left(range(max(nums)), k, key=solve)
        # -----参考答案------

        # 这不就是，选择k个不相邻的，取最大，所有可能情况中选最小
        ans = inf
        tmp = [inf] * k
        n = len(nums)

        def dfs(i:int, times:int):
            nonlocal ans
            if i<0 or times >=k:
                if times>=k:
                    ans = min(ans, (max(tmp)))
                    # print("tmp:", tmp)
                    # print("ans:", ans)
                return
            # 选i
            if nums[i] < ans:
                tmp[times] = nums[i]
                dfs(i-2, times+1)
                tmp[times] = inf
            # 不选i
            dfs(i-1, times)

        dfs(n-1, 0)
        return ans
# @lc code=end
import sys
import json
nums = sys.stdin.readline()
k = eval(input())
nums = json.loads(nums)
sol = Solution()
print(sol.minCapability(nums, k))


#
# @lcpr case=start
# [2,3,5,9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n2\n
# @lcpr case=end

#


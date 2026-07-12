#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30404
#
# [128] 最长连续序列
# 14:46 仍然超时，因为没有去重
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 参考答案
        st = set(nums)
        m = len(st)
        ans = 0
        for x in st:
            if x-1 in st:
                continue
            y = x+1
            while y in st:
                y += 1
            ans = max(ans, y-x)
            if ans * 2 >= m:
                break
        return ans

        # 我的上一次答案
        hash_map = set(nums)
        nums = list(hash_map)
        ans = 0
        for x in nums:
            if x-1 not in hash_map:
                y = x+1
                while y in hash_map:
                    y += 1
                ans = max(ans, y-x)
        return ans
        
        # 仍旧一个哈希的表
        hash_map = {}
        for n in nums:
            hash_map[n] = 1
        ans = 0
        for n in nums:
            if n-1 in hash_map:
                continue
            cur = n+1
            while cur in hash_map:
                cur += 1
            ans = max(ans, cur - n)
        return ans
# @lc code=end

import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.longestConsecutive(nums))

#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#


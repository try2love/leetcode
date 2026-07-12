#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30404
#
# [1] 两数之和
# 11:33 ACM AC
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 参考答案
        idx = {} # 空哈希表 字典
        for j, x in enumerate(nums):
            if target - x in idx:
                return [idx[target-x], j]
            idx[x] = j
        return

        # 哈希表o(1)查找
        ans = []
        hash_map = defaultdict(list)
        for idx, n in enumerate(nums[::-1]):
            hash_map[n].append(len(nums)-idx-1)
        for idx, n in enumerate(nums):
            hash_map[n].pop()
            if target - n in hash_map and len(hash_map[target-n])!=0:
                return [idx, hash_map[target-n][0]]
        

# @lc code=end
# import sys
# nums = sys.stdin.readline().strip().split()
# # print(nums)
# nums = [int(n) for n in nums]
# target = int(input())
# sol = Solution()
# print(sol.twoSum(nums, target))
import sys
import json
nums = json.loads(sys.stdin.readline().strip())
target = eval(input())
sol = Solution()
print(sol.twoSum(nums, target))


#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#


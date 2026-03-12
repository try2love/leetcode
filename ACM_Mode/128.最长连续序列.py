#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30400
#
# [128] 最长连续序列
from typing import List
from collections import defaultdict
from functools import cache
# @lc code=start

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)  # 把 nums 转成哈希集合
        ans = 0
        for x in st:  # 遍历哈希集合
            if x - 1 in st:  # 如果 x 不是序列的起点，直接跳过
                continue
            # x 是序列的起点
            y = x + 1
            while y in st:  # 不断查找下一个数是否在哈希集合中
                y += 1
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            ans = max(ans, y - x)  # 从 x 到 y-1 一共 y-x 个数
        return ans
    
# @lc code=end

# import sys
# data = sys.stdin.readline().strip().split()
# # data = [int(x) for x in data]
# data = list(map(int, data))
# solution = Solution()
# result = solution.longestConsecutive(data)
# print(result)

import sys
line = sys.stdin.readline().strip()
if not line:
    data = []
else:
    data = [int(x.strip()) for x in line.split()]
solution = Solution()
result = solution.longestConsecutive(data)
print(result)


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


#
# @lc app=leetcode.cn id=167 lang=python3
# @lcpr version=30404
#
# [167] 两数之和 II - 输入有序数组
# 8:11 ACM AC
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 参考答案
        left = 0
        right = len(numbers)-1
        while True:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            if s > target:
                right -= 1
            else:
                left += 1

        # pos = defaultdict(int)
        # for i in range(len(numbers)-1, -1, -1):
        #     pos[numbers[i]] = i+1
        # for key in pos:
        #     if target - key in pos:
        #         return [pos[target-key], pos[key]]
        pos = defaultdict(list)
        for i in range(len(numbers)):
            pos[numbers[i]].append(i+1)
        for key in pos:
            if target-key in pos:
                if target-key == key:
                    if len(pos[key]) >= 2:
                        return [pos[key][0], pos[key][1]]
                else:
                    return [pos[key][0], pos[target-key][0]]
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n-1\n
# @lcpr case=end

#


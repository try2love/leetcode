#
# @lc app=leetcode.cn id=169 lang=python3
# @lcpr version=30403
#
# [169] 多数元素
# 4:28 ACM AC
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # -----参考答案------
        ans = hp = 0
        for x in nums:
            if hp == 0:
                ans, hp = x, 1
            else:
                hp += 1 if x == ans else -1
        return ans
        # -----参考答案------

        # 一个counter即可解决
        # 实在想不起来o1的做法
        cnt = Counter(nums)
        for x in cnt:
            if cnt[x] > len(nums)//2:
                return x
        return -1

# @lc code=end
import sys
import json
nums = json.loads(sys.stdin.readline().strip())
sol = Solution()
print(sol.majorityElement(nums))


#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30404
#
# [219] 存在重复元素 II
# 4:38 ACM AC
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 参考答案
        st = set()
        for i,x in enumerate(nums):
            if x in st:
                return True
            st.add(x)
            if i >= k:
                st.remove(nums[i-k])
        return False

        last = {}
        for i,x in enumerate(nums):
            if x in last and i-last[x] <= k:
                return True
            last[x] = i
        return False

        # 长度为k+1的滑动窗口中找是否有重复元素
        cnt = defaultdict(int)
        if k >= len(nums):
            return len(set(nums)) < len(nums)
        for i in range(k+1):
            cnt[nums[i]] += 1
            if cnt[nums[i]] >= 2:
                return True
        for j in range(k+1, len(nums)):
            cnt[nums[j-k-1]] -= 1
            cnt[nums[j]] += 1
            if cnt[nums[j]] >= 2:
                return True
        return False
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#


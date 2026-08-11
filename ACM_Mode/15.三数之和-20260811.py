#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30404
#
# [15] 三数之和
# 10:50 Memory Limit Exceeded

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        # cankao
        ans = []
        for i in range(n-2):
            x = nums[i]
            if i>0 and x == nums[i-1]:
                continue
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[-2] + nums[-1] < 0:
                continue
            j = i+1
            k = n-1
            while j<k:
                s = x+nums[j]+nums[k]
                if s>0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x,nums[j],nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k -= 1
        return ans

        if nums[-1] < 0 or nums[0] > 0:
            return []
        ans = []
        i=0
        while i < n:
            x = nums[i]
            if x > 0:
                break
            left = i+1
            right = n-1
            while left < right:
                if nums[left] + nums[right] == -x:
                    ans.append([x, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -x:
                    right -= 1
                else:
                    left += 1
                while left < right and nums[right-1] == nums[right]:
                    right -= 1
                while left < right and nums[left+1] == nums[left]:
                    left += 1
            i += 1
            while i<n and nums[i-1] == nums[i]:
                i += 1
        return ans

# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#


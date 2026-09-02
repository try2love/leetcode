#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30404
#
# [15] 三数之和
# 8:28 ACMAC

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 参考答案
        nums.sort()
        ans = []
        n = len(nums)
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
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
        return ans
    
        nums.sort()
        i = 0
        j = i+1
        k = len(nums)-1
        ans = []
        while i < len(nums)-2 and nums[i] <= 0:
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                    while k>j and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
            i += 1
            while i < len(nums)-2 and nums[i-1] == nums[i]:
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


#
# @lc app=leetcode.cn id=763 lang=python3
# @lcpr version=30403
#
# [763] 划分字母区间
# 11:22 ACM AC
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # -----参考答案------
        last = {c: i for i,c in enumerate(s)} # 每个字母最后出现的下标
        ans = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c]) # 更新当前区间右端点的最大值
            if end == i:
                ans.append(end-start+1) # 区间长度加入答案
                start = end + 1
        return ans
        # -----参考答案------

        if len(s) == 0:
            return 0
        # 哈希表+贪心
        hash_map = defaultdict(list)
        for idx, x in enumerate(s):
            if x in hash_map:
                hash_map[x][1] = idx
            else:
                hash_map[x] = [idx, idx]
        start = 0
        end = hash_map[s[0]][1]
        ans = []
        idx = 1
        for idx, x in enumerate(s):
            if idx == 0:
                continue
            cur_start, cur_end = hash_map[x]
            if cur_start > end:
                ans.append(cur_start-start)
                start = cur_start
                end = cur_end
            end = max(end, cur_end)
        ans.append(len(s) - sum(ans))
        return ans
            
# @lc code=end

s = input()
sol = Solution()
print(sol.partitionLabels(s))

#
# @lcpr case=start
# "ababcbacadefegdehijhklij"\n
# @lcpr case=end

# @lcpr case=start
# "eccbbbbdec"\n
# @lcpr case=end

#


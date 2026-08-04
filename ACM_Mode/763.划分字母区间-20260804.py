#
# @lc app=leetcode.cn id=763 lang=python3
# @lcpr version=30404
#
# [763] 划分字母区间
# 14:32 ACM AC
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 参考答案
        last = {c: i for i,c in enumerate(s)}
        ans = []
        start = end = 0
        for i,c in enumerate(s):
            end = max(end, last[c])
            if end == i:
                ans.append(end-start+1)
                start = end + 1
        return ans

        ans = []
        # 感觉本质上也是在搭梯子
        cnt = defaultdict(int)
        for idx, x in enumerate(s):
            cnt[x] = idx
        right = 0
        idx = 0
        while idx < len(s):
            right = max(right, cnt[s[idx]])
            idx += 1
            if idx > right:
                if len(ans):
                    ans.append(idx-sum(ans))
                else:
                    ans.append(idx)
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


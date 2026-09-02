#
# @lc app=leetcode.cn id=30 lang=python3
# @lcpr version=30404
#
# [30] 串联所有单词的子串
# 21:52 46/182 cases passed (N/A)
from typing import List
from collections import defaultdict,Counter
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 参考答案
        # word_len = len(words[0])
        # window_len = word_len * len(words)
        # target_cnt = Counter(words)
        # ans = []
        # for start in range(word_len):
        #     cnt = defaultdict(int)
        #     overload = 0
        #     for right in range(start+word_len, len(s)+1, word_len):
        #         in_word = s[right-word_len:right]
        #         if cnt[in_word] == target_cnt[in_word]:
        #             overload += 1
        #         cnt[in_word] += 1
        #         left = right - window_len
        #         if left < 0:
        #             continue
        #         if overload == 0:
        #             ans.append(left)
        #         out_word = s[left: left+word_len]
        #         cnt[out_word] -= 1
        #         if cnt[out_word] == target_cnt[out_word]:
        #             overload -= 1
        # return ans

        cnt = defaultdict(int)
        word_cnt = Counter(words)
        x = len(words[-1])
        left = 0
        pre = s[left*x:(left+1)*x]
        right = len(words) - 1
        for i in range(left, right+1):
            cur = s[i*x:(i+1)*x]
            cnt[cur] += 1
        ans = []
        if cnt == word_cnt:
            ans.append(0)
        for right in range(len(words), len(s)//x+1):
            cnt[pre] -= 1
            if cnt[pre] == 0:
                del cnt[pre]
            left += 1
            pre = s[left*x:(left+1)*x]
            cur = s[right*x:(right+1)*x]
            cnt[cur] += 1
            if cnt == word_cnt:
                # print(left*x)
                ans.append(left*x)
        return ans
        
# @lc code=end

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
sol = Solution()
print(sol.findSubstring(s, words))

#
# @lcpr case=start
# "barfoothefoobarman"\n["foo","bar"]\n
# @lcpr case=end

# @lcpr case=start
# "wordgoodgoodgoodbestword"\n["word","good","best","word"]\n
# @lcpr case=end

# @lcpr case=start
# "barfoofoobarthefoobarman"\n["bar","foo","the"]\n
# @lcpr case=end

#


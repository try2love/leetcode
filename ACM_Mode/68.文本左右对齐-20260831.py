#
# @lc app=leetcode.cn id=68 lang=python3
# @lcpr version=30404
#
# [68] 文本左右对齐
# 20:56 ACM AC
from typing import List
# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 参考答案
        ans = []
        n = len(words)
        i = 0
        while i < n:
            start = i  # 这一行第一个单词的下标
            sum_len = -1  # 第一个单词之前没有空格
            while i < n and sum_len + len(words[i]) + 1 <= maxWidth:
                sum_len += len(words[i]) + 1  # 单词之间至少要有一个空格
                i += 1

            extra_spaces = maxWidth - sum_len  # 这一行剩余未分配的空格个数
            gaps = i - start - 1  # 这一行单词之间的空隙个数（单词个数减一）

            # 特殊情况：如果只有一个单词，或者是最后一行，那么左对齐，末尾补空格
            if gaps == 0 or i == n:
                row = ' '.join(words[start: i]) + ' ' * extra_spaces  # 末尾补空格
                ans.append(row)
                continue

            # 一般情况：把 extra_spaces 个空格均匀分配到 gaps 个空隙中（靠左的空格更多）
            avg, rem = divmod(extra_spaces, gaps)
            spaces = ' ' * (avg + 1)  # +1 表示加上单词之间已有的一个空格
            # 前 rem 个空隙多一个空格
            row = (spaces + ' ').join(words[start: start + rem + 1]) + \
                  spaces + spaces.join(words[start + rem + 1: i])
            ans.append(row)
        return ans

        word_length = [len(word) for word in words]
        ans = []
        row = []
        row_len = 0
        for i, x in enumerate(words):
            row.append(x)
            row_len += word_length[i]
            if row_len + len(row) - 1 > maxWidth:
                row.pop()
                row_len -= word_length[i]
                space = len(row) - 1
                if space == 0:
                    ans.append(row[0] + " " * (maxWidth-row_len))
                else:
                    tmp = (maxWidth - row_len) // space
                    tmp2 = (maxWidth-row_len)%space
                    if tmp2 == 0:
                        s = " "*tmp
                        ans.append(s.join(row))
                    else:
                        s= ""
                        for y in row:
                            s += y
                            s += ' ' * tmp
                            if tmp2>0:
                                s += ' '
                                tmp2 -= 1
                        ans.append(s[:maxWidth])
                row = [x]
                row_len = len(x)
        if row:
            ans.append(" ".join(row))
        if len(ans[-1]) < maxWidth:
            ans[-1] += " "*(maxWidth-len(ans[-1]))
        return ans
        
# @lc code=end
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
sol = Solution()
print(sol.fullJustify(words, maxWidth))


#
# @lcpr case=start
# ["This", "is", "an", "example", "of", "text", "justification."]\n16\n
# @lcpr case=end

# @lcpr case=start
# ["What","must","be","acknowledgment","shall","be"]\n16\n
# @lcpr case=end

# @lcpr case=start
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]\n20\n
# @lcpr case=end

#


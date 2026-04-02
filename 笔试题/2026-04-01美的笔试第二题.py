# 输入s和一个数组a，判断能不能把s分割，得到的结果是a的子集

import sys

def solve():
    s = sys.stdin.readline().strip()
    a = sys.stdin.readline().strip().split(",")
    def dfs(i:int):
        # 表示从i号位置开始的字符串
        if i >= len(s):
            return True
        tmp = []
        for x in a:
            if s[i:i+len(x)] == x:
                tmp.append(dfs(i+len(x)))
        return any(tmp)
    return dfs(0)


if __name__ == "__main__":
    print(int(solve()))
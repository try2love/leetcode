"""
荣耀技术笔试第三题：
模拟C语言的引用

输入一行字符串：
a b;a c;b e;e b;c d;d a
分别表示在a里面include了b，在a里面include了c，以此类推。

输出：
EXPAND:a b e c d
CIRCLE:b e b;a c d a

前者表示从第一个文件开始的逐个引用关系，后者表示存在的闭环引用链路。如果没有闭环引用，则只用输出CIRCLE:
注意，对于第一个输入作为文件，一定有对所有其他头文件的引用链路（也就是说EXPAND一定是包含所有数据数据的）
"""

import sys

def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    # 1. 解析输入建图
    pairs = line.split(';')
    adj = {}
    first_node = pairs[0].split()[0]
    
    for p in pairs:
        u, v = p.split()
        if u not in adj: adj[u] = []
        adj[u].append(v)
        if v not in adj: adj[v] = []

    path = []
    circle = []
    tmp = []
    def dfs(first_node):
        nonlocal tmp
        if first_node in tmp:
            cur = [first_node]
            for x in tmp[::-1]:
                cur.append(x)
                if x == first_node:
                    break
            circle.append(cur[::-1])
            tmp = tmp[:len(tmp)-len(cur)+1]
            return
        path.append(first_node)
        tmp.append(first_node)
        for second_node in adj[first_node]:
            dfs(second_node)
    dfs(first_node)
    print("EXPAND:"+" ".join(path))
    print("CIRCLE:",end="")
    s = ""
    for i in range(len(circle)):
        s += " ".join(circle[i])
        s += ";"
    print(s[:-1])

if __name__ == "__main__":
    solve()
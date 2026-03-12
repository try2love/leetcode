可以。下面我只讲 **Python3 的 ACM 模式模板**，尽量整理成你刷题时能直接拿来用的形式。

你现在的目标不是学算法，而是先把 **输入输出框架**彻底固定下来。
只要这个框架熟了，Hot100 里的题换成 ACM 模式，本质上只是“把函数题改成完整程序题”。

------

# 一、Python3 写 ACM 的总原则

最推荐你养成这个结构：

```python
import sys
input = sys.stdin.readline

def solve():
    # 处理一组测试数据
    pass

solve()
```

如果是多组测试，就把外层改掉：

```python
import sys
input = sys.stdin.readline

def solve():
    # 处理一组测试数据
    pass

T = int(input().strip())
for _ in range(T):
    solve()
```

也就是说：

- `solve()` 负责“做一组数据”
- 外层负责“做几组数据”

这是最重要的习惯。

------

# 二、最基础模板

## 1. 单组测试模板

适用于题目只有一组输入。

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(sum(nums))

solve()
```

------

## 2. 多组测试模板：第一行给 T

这是最常见的模板。

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(sum(nums))

T = int(input().strip())
for _ in range(T):
    solve()
```

### 什么时候用这个

看到题目写：

- 第一行输入一个整数 `T`
- 接下来有 `T` 组测试数据

就直接用这个。

------

## 3. 多组测试模板：直到 EOF

这个也非常常见，尤其是牛客、杭电、洛谷部分题。

```python
import sys
input = sys.stdin.readline

def solve(n):
    nums = list(map(int, input().split()))
    print(sum(nums))

while True:
    try:
        line = input()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
        n = int(line)
        solve(n)
    except EOFError:
        break
```

其实如果用了 `sys.stdin.readline`，更常见是靠 `if not line: break` 来结束。
因为文件结束时，`readline()` 会返回空字符串。

------

# 三、你最关心的：多个测试用例到底怎么判断

这件事一定要看题目输入描述。

## 情况 1：第一行明确给 `T`

例如：

```text
3
5
1 2 3 4 5
4
2 7 11 15
3
3 2 4
```

那就是：

```python
T = int(input().strip())
for _ in range(T):
    solve()
```

------

## 情况 2：没有 `T`，但说“多组输入直到 EOF”

例如输入是：

```text
5
1 2 3 4 5
4
2 7 11 15
3
3 2 4
```

没有告诉你一共有几组，那就只能一直读，直到结束：

```python
while True:
    line = input()
    if not line:
        break
    ...
```

或者：

```python
while True:
    try:
        ...
    except EOFError:
        break
```

------

## 情况 3：每一行就是一组数据

例如：

```text
1 2 3
4 5
10 20 30 40
```

那就按行处理：

```python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    nums = list(map(int, line.split()))
    print(sum(nums))
```

------

# 四、最推荐你背下来的 Python3 模板

下面这些是真正高频的。

------

## 模板 A：单组测试

```python
import sys
input = sys.stdin.readline

def solve():
    pass

solve()
```

------

## 模板 B：T 组测试

```python
import sys
input = sys.stdin.readline

def solve():
    pass

T = int(input().strip())
for _ in range(T):
    solve()
```

------

## 模板 C：直到 EOF

```python
import sys
input = sys.stdin.readline

def solve(line):
    n = int(line)
    nums = list(map(int, input().split()))
    print(sum(nums))

while True:
    line = input()
    if not line:
        break
    line = line.strip()
    if not line:
        continue
    solve(line)
```

------

## 模板 D：按行处理直到 EOF

```python
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    nums = list(map(int, line.split()))
    print(sum(nums))
```

------

# 五、为什么推荐 `sys.stdin.readline`

因为 Python 默认的 `input()` 在数据量大时可能偏慢。
ACM/笔试里，最常见写法是：

```python
import sys
input = sys.stdin.readline
```

之后你仍然像平时一样用：

```python
n = int(input().strip())
nums = list(map(int, input().split()))
```

这里注意两点：

### 1. `int(input())` 最好改成 `int(input().strip())`

因为 `readline()` 读出来通常末尾带换行符。

### 2. `input().split()` 通常不用 `strip()`

因为 `split()` 本身会处理空白字符。

例如这句完全没问题：

```python
nums = list(map(int, input().split()))
```

------

# 六、常用输入模板

下面是你刷题时最常见的数据类型。

------

## 1. 读一个整数

```python
n = int(input().strip())
```

------

## 2. 读一行多个整数

```python
a, b = map(int, input().split())
```

或者：

```python
nums = list(map(int, input().split()))
```

------

## 3. 读一个长度为 n 的数组

```python
n = int(input().strip())
nums = list(map(int, input().split()))
```

如果题目保证第二行正好有 n 个数，这样写就行。

------

## 4. 读二维数组

```python
n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
```

也可以写成：

```python
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
```

------

## 5. 读字符串

```python
s = input().strip()
```

------

## 6. 读字符数组

```python
s = input().strip()
chars = list(s)
```

------

## 7. 读一行字符串列表

```python
words = input().split()
```

------

## 8. 读矩阵字符图

比如：

```text
3 4
abcd
efgh
ijkl
```

写法：

```python
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
```

如果要转成可修改的二维字符数组：

```python
grid = [list(input().strip()) for _ in range(n)]
```

------

# 七、输出模板

ACM 输出最怕格式错。

------

## 1. 输出一个数

```python
print(ans)
```

------

## 2. 输出一行多个数

```python
print(*nums)
```

例如：

```python
nums = [1, 2, 3]
print(*nums)
```

输出：

```text
1 2 3
```

------

## 3. 输出多行

```python
for x in ans:
    print(x)
```

------

## 4. 先收集再统一输出

数据量大时推荐：

```python
res = []
for _ in range(T):
    res.append(str(ans))
print('\n'.join(res))
```

这个能减少很多次 `print()` 的开销。

------

# 八、数组题模板

这是你现在刷 Hot100 最常用的。

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    nums = list(map(int, input().split()))

    ans = sum(nums)
    print(ans)

solve()
```

多组测试版：

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(sum(nums))

T = int(input().strip())
for _ in range(T):
    solve()
```

------

# 九、字符串题模板

```python
import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    print(s[::-1])

solve()
```

多组测试：

```python
import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    print(s[::-1])

T = int(input().strip())
for _ in range(T):
    solve()
```

------

# 十、二维矩阵题模板

```python
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += grid[i][j]

    print(ans)

solve()
```

------

# 十一、图论题模板

## 1. 无向图

```python
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    print(g)

solve()
```

------

## 2. 有向图

```python
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)

    print(g)

solve()
```

------

## 3. 加权图

```python
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))  # 无向图

    print(g)

solve()
```

------

# 十二、二叉树题在 ACM 里怎么处理

LeetCode 里二叉树题一般系统已经帮你建好树。
ACM 模式下通常要自己根据输入建树。

最常见的做法是：**层序数组建树**。

比如输入：

```text
1 2 3 null 4
```

可以这样处理：

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(vals):
    if not vals or vals[0] == 'null':
        return None

    root = TreeNode(int(vals[0]))
    q = deque([root])
    i = 1

    while q and i < len(vals):
        node = q.popleft()

        if i < len(vals) and vals[i] != 'null':
            node.left = TreeNode(int(vals[i]))
            q.append(node.left)
        i += 1

        if i < len(vals) and vals[i] != 'null':
            node.right = TreeNode(int(vals[i]))
            q.append(node.right)
        i += 1

    return root
```

读取：

```python
vals = input().split()
root = build_tree(vals)
```

这个不是每题都用，但你做树题时很常见。

------

# 十三、链表题在 ACM 里怎么处理

LeetCode 里链表是现成的，ACM 里通常会给你数组，你自己转链表。

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(nums):
    dummy = ListNode()
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(' '.join(res))
```

------

# 十四、真正高性能的万能读法

当输入特别大时，可以直接一次性读完。

```python
import sys

data = sys.stdin.read().split()
idx = 0

n = int(data[idx])
idx += 1

nums = list(map(int, data[idx:idx+n]))
idx += n

print(sum(nums))
```

如果是多组测试：

```python
import sys

data = sys.stdin.read().split()
idx = 0

T = int(data[idx])
idx += 1

res = []
for _ in range(T):
    n = int(data[idx])
    idx += 1

    nums = list(map(int, data[idx:idx+n]))
    idx += n

    res.append(str(sum(nums)))

print('\n'.join(res))
```

### 这个写法的特点

优点：

- 很快
- 很适合大输入

缺点：

- 不够直观
- 不适合你现在刚熟悉 ACM 模式时使用

你现在先以 `readline + solve()` 为主，后面再练这种。

------

# 十五、容易踩的坑

## 1. 忘了看是不是多组测试

这是最常见的问题。
代码没错，但题目有多组，你只处理了一组，就会 WA。

------

## 2. `readline()` 返回空字符串表示 EOF

所以这种写法要会看：

```python
line = input()
if not line:
    break
```

------

## 3. 空行问题

有些平台输入里可能混入空行，所以更稳一点是：

```python
line = line.strip()
if not line:
    continue
```

------

## 4. 输出数组时不要自己手搓空格

直接：

```python
print(*nums)
```

最省心。

------

## 5. 多组输出时，尽量统一收集后再输出

例如：

```python
res = []
for _ in range(T):
    res.append(str(ans))
print('\n'.join(res))
```

------

# 十六、拿“数组求和”这题举例

------

## 1. 单组测试

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(sum(nums))

solve()
```

------

## 2. 第一行是 T

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(sum(nums))

T = int(input().strip())
for _ in range(T):
    solve()
```

------

## 3. 直到 EOF

```python
import sys
input = sys.stdin.readline

while True:
    line = input()
    if not line:
        break
    line = line.strip()
    if not line:
        continue

    n = int(line)
    nums = list(map(int, input().split()))
    print(sum(nums))
```

------

# 十七、我建议你刷题时固定使用这一套

你现在先只记这套就够了。

## 标准版

```python
import sys
input = sys.stdin.readline

def solve():
    pass

solve()
```

## 多测版

```python
import sys
input = sys.stdin.readline

def solve():
    pass

T = int(input().strip())
for _ in range(T):
    solve()
```

## EOF 版

```python
import sys
input = sys.stdin.readline

while True:
    line = input()
    if not line:
        break
    line = line.strip()
    if not line:
        continue

    # 根据这一行开始处理一组数据
```

你只要把这三套彻底练熟，Python3 的 ACM 输入输出就已经过关了。

------

# 十八、给你一个最实用的判断口诀

看输入描述时，只问自己这三个问题：

## 第一问：有没有 `T`

有，就：

```python
T = int(input().strip())
for _ in range(T):
    solve()
```

## 第二问：是不是直到 EOF

是，就：

```python
while True:
    line = input()
    if not line:
        break
```

## 第三问：是不是每行一组

是，就：

```python
for line in sys.stdin:
    ...
```

------

下一步最适合做的，就是把 **Hot100 常见题型在 Python3 下改写成 ACM 模式模板**。
比如数组、链表、二叉树、回溯、图、DFS/BFS、DP，各自怎么写输入输出。
## 2026-01-18

### python中的哈希表

#### **一、Python 哈希表的本质**

在 Python 中，所谓的“哈希表”主要对应两种内置数据结构：**dict（字典）** 和 **set（集合）**。它们的底层实现都基于哈希表技术，因此在平均情况下可以提供 **O(1)** 时间复杂度的增删改查操作。

哈希表的核心思想是：

将一个键（key）通过哈希函数映射为一个整数索引，然后把对应的值（value）存储到该索引位置。这样在查找时，不需要线性遍历整个数据结构，只需要再次计算哈希值，就可以快速定位到目标元素。

Python 的字典并不是简单的“数组 + 哈希函数”，而是一个经过高度优化的复杂结构，内部包含以下几个关键概念：

- 哈希函数：hash(key)
- 哈希桶（bucket）
- 冲突处理机制
- 动态扩容策略

因此，Python 中的字典是一种高度工程化的哈希表实现。

#### **二、什么样的对象可以作为哈希表的键**

并不是所有 Python 对象都可以作为字典的 key。能够作为 key 的对象必须满足两个条件：

- 对象必须是 **可哈希的（hashable）**
- 对象必须是 **不可变的（immutable）**

常见可以作为 key 的类型包括：

- int
- float
- str
- tuple（前提是 tuple 内部元素也都是可哈希的）
- frozenset

常见不能作为 key 的类型包括：

- list
- dict
- set

原因是这些类型是可变对象，而哈希值必须在对象生命周期内保持不变。

可以通过 hash() 函数判断一个对象是否可哈希：

```
hash(10)        # 合法
hash("hello")   # 合法
hash([1,2,3])   # 报错：list 不可哈希
```

#### **三、字典的创建方式**

Python 提供了多种创建字典的方法。

最常见的字面量创建方式：

```
d = {"a": 1, "b": 2}
```

使用构造函数创建：

```
d = dict(a=1, b=2)
```

从键值对序列创建：

```
d = dict([("a", 1), ("b", 2)])
```

创建空字典：

```
d = {}
d = dict()
```

#### **四、哈希表的基本操作**

下面系统介绍 Python 字典的增删改查操作。

##### **4.1 插入和修改操作**

在 Python 中，插入和修改的语法完全相同：

```
d = {}

d["name"] = "Tom"
```

如果 key 不存在，这一行代码会执行插入操作；

如果 key 已经存在，这一行代码会执行修改操作。

例如：

```
d["age"] = 20
d["age"] = 21
```

第一行是插入，第二行是修改。

这种设计体现了 Python 字典的一个特点：

**字典不会允许重复 key，新的值会覆盖旧值。**

##### **4.2 查询操作**

最直接的查询方式：

```
value = d["name"]
```

这种方式的特点是：

- 如果 key 存在，返回对应 value
- 如果 key 不存在，抛出异常

例如：

```
d = {"a": 1}
print(d["b"])
```

会抛出异常：

```
KeyError: 'b'
```

为了避免异常，Python 提供了更安全的查询方式。

###### **使用 get 方法查询**

```
value = d.get("b")
```

当 key 不存在时，get 方法会返回：

```
None
```

也可以指定默认值：

```
value = d.get("b", 0)
```

这时如果 key 不存在，会返回 0。

###### **判断 key 是否存在**

推荐使用：

```
if "name" in d:
    ...
```

不要使用 d.keys() 再去判断，这样效率更低。

##### **4.3 删除操作**

删除某个键：

```
del d["name"]
```

如果 key 不存在，del 会抛出 KeyError。

更安全的删除方式是 pop：

```
value = d.pop("name", None)
```

含义是：

- 如果 key 存在，删除并返回对应 value
- 如果 key 不存在，返回 None（或自定义默认值）

清空整个字典：

```
d.clear()
```

#### **五、如果访问一个不存在的键会发生什么**

这是一个非常重要的问题。

当使用中括号方式访问时：

```
d["x"]
```

如果 key 不存在，Python 会直接抛出：

```
KeyError
```

这是一种运行时异常，必须显式处理。

而使用 get 方法时：

```
d.get("x")
```

不会抛异常，而是返回 None。

因此在实际开发中：

- 如果你确信 key 一定存在，可以直接用 d[key]
- 如果 key 可能不存在，建议使用 get 或 in 判断

#### **六、遍历字典**

Python 字典提供了多种遍历方式。

遍历所有 key：

```
for k in d:
    print(k)
```

遍历所有 value：

```
for v in d.values():
    print(v)
```

同时遍历 key 和 value：

```
for k, v in d.items():
    print(k, v)
```

这种方式是最常用、也是最推荐的。

#### **七、时间复杂度分析**

在平均情况下，字典的操作时间复杂度如下：

| **操作** | **时间复杂度** |
| -------- | -------------- |
| 插入     | O(1)           |
| 查找     | O(1)           |
| 删除     | O(1)           |
| 遍历     | O(n)           |

需要注意的是：

在极端情况下（大量哈希冲突），这些操作可能退化为 O(n)，但在实际 Python 实现中几乎不会发生。

#### **八、哈希冲突与解决机制**

哈希冲突是指：

不同的 key 经过 hash() 计算后得到相同的哈希值。

Python 采用的冲突解决策略是：

- 开放寻址法（open addressing）
- 探测序列（probing sequence）

当发生冲突时，Python 会尝试新的位置存储数据，而不是像链地址法那样使用链表。

#### **九、字典的扩容机制**

当字典中元素越来越多时，会自动触发扩容。

扩容的特点：

- 新建一个更大的哈希表
- 重新计算所有 key 的哈希位置
- 把旧数据迁移到新表中

因此，扩容是一个相对耗时的操作，但发生频率很低。

#### **十、字典的顺序性**

从 Python 3.7 开始，字典是**有序的**：

插入顺序会被保留：

```
d = {"a":1, "b":2, "c":3}
```

遍历时顺序一定是 a → b → c。



但这并不改变字典是哈希表的本质，只是实现细节做了优化。

#### **十一、set 与 dict 的关系**

set 本质上可以看作：

- 只有 key
- 没有 value 的字典

因此 set 的操作与 dict 非常相似：

```
s = set()
s.add(10)
s.remove(10)
```

set 的底层同样是哈希表。

#### **十二、常见陷阱和注意事项**

不要使用可变对象作为 key：

```
d = {}
d[[1,2]] = 10
```

这会直接报错。

不要依赖 id() 作为 key，因为对象的 id 可能变化。

字典查找时不要这样写：

```
if key in d.keys():
```

直接写：

```
if key in d:
```

效率更高。

#### **十三、总结**

Python 的哈希表是一个高度优化的数据结构，提供了：

- 平均 O(1) 的增删改查性能
- 自动扩容机制
- 内置冲突处理
- 有序性保证

在实际编程中，dict 是 Python 最重要的数据结构之一，理解它的行为规则，对写出高效稳定的 Python 程序至关重要。

### defaultdict创建字典和sorted排序函数

#### **一、defaultdict 的定位与核心思想**

defaultdict 位于 Python 标准库 collections 中，它是 dict 的一个子类，主要解决的问题是：当访问一个不存在的键时，普通 dict 会抛出 KeyError，而 defaultdict 可以自动为该键创建一个默认值，从而让“初始化再更新”的代码变得更简洁、更不容易出错。defaultdict 的关键在于一个初始化参数 default_factory，它必须是一个可调用对象，用于在缺失键被访问时生成默认值。

普通 dict 的典型模式经常是先判断 key 是否存在，再初始化，然后再追加或累加，这会产生大量重复代码。defaultdict 把这类“模式化初始化”内置化，使得代码结构更稳定，也更适合高频统计、分组、聚合等任务。

#### **二、defaultdict 的基本用法与行为细节**

defaultdict 的创建形式通常是 defaultdict(factory)，其中 factory 是一个可调用对象。最常见的 factory 有 list、set、int、dict，也可以是自定义函数或 lambda。举例来说，当 factory 为 list 时，每个新键的默认值都是一个全新的空列表，而不是共享同一个对象，这一点非常关键，因为它避免了默认可变对象带来的共享引用问题。

当你对一个不存在的键进行索引访问时，defaultdict 会执行以下动作：先调用 default_factory 生成默认值，把这个默认值写入字典，再把默认值返回给调用者。因此，与 dict.get 不同，defaultdict 的缺失键访问会产生副作用，它会改变字典内容。

示例，按 key 分组收集元素

```
from collections import defaultdict

groups = defaultdict(list)
pairs = [("a", 1), ("b", 2), ("a", 3)]

for k, v in pairs:
    groups[k].append(v)

print(groups)  # {'a': [1, 3], 'b': [2]}
```

此处的 groups[“a”] 初次访问时会自动生成空列表并写入，然后 append 才能直接使用。

#### **三、defaultdict 常用 factory 的语义对照**

default_factory 为 list 时，适用于分组和收集，典型操作是 append。default_factory 为 set 时，适用于去重收集，典型操作是 add。default_factory 为 int 时，适用于计数累加，因为 int() 返回 0，典型操作是加一或加某个权重。default_factory 为 dict 时，适用于构造嵌套字典结构，但如果嵌套层数更深，通常会用递归 factory 或者显式构造来避免结构难以维护。

计数示例

```
from collections import defaultdict

cnt = defaultdict(int)
for x in ["a", "b", "a", "c", "a"]:
    cnt[x] += 1

print(cnt)  # {'a': 3, 'b': 1, 'c': 1}
```

去重分组示例

```
from collections import defaultdict

groups = defaultdict(set)
pairs = [("a", 1), ("a", 1), ("a", 2)]
for k, v in pairs:
    groups[k].add(v)

print(groups)  # {'a': {1, 2}}
```

#### **四、defaultdict 与 dict.get 的差异与选择建议**

dict.get(key, default) 的行为是：如果 key 不存在，返回 default，但不会把 key 写入字典，因此它没有副作用，更适合“查询型逻辑”。defaultdict 的缺失键访问会写入键值对，更适合“构建型逻辑”，例如统计、聚合、建索引、分桶。

也就是说，如果你只是想安全读取而不想改变结构，使用 get 更合适；如果你希望缺失键自动初始化并继续更新，defaultdict 的表达会更直接。

另外，defaultdict 的 default_factory 必须可调用，如果传入 None，则 defaultdict 的行为会退化成普通 dict，缺失键仍会抛 KeyError。某些场景下你希望保留 defaultdict 的类型但不希望自动创建默认值，可以显式设置 default_factory 为 None。

#### **五、defaultdict 的常见陷阱与注意事项**

最容易忽略的点是缺失键访问会导致字典发生变化，例如仅仅执行一次 print(groups[“missing”]) 就会把 missing 写进字典，这在调试或统计过程中可能造成意外键出现。其次，default_factory 返回的对象必须是你期望的类型，例如用 list 时应当使用 append，而不是 add。再者，默认值的生成发生在访问阶段，而不是创建阶段，因此不存在共享同一个默认对象的问题，这是它比手写默认参数更安全的原因之一。

如果你使用自定义 factory，要确保它每次调用都返回一个全新的对象，除非你明确希望共享。例如 factory 返回同一个列表对象会导致不同键共享同一份数据，通常这是错误的。

#### **六、sorted 的定位与核心思想**

sorted 是 Python 内置排序函数，用于对任何可迭代对象进行排序，并返回一个新的列表。它不会修改原对象，因此是一种非破坏性操作。与之对应的是列表方法 list.sort，它会原地排序并返回 None。sorted 的优势在于适用范围广，可以对列表、元组、字符串、生成器、字典的键视图或值视图等进行排序。

sorted 的签名可以理解为 sorted(iterable, key=None, reverse=False)，其中 key 是一个函数，用来指定排序依据；reverse 用来控制升序或降序。

#### **七、sorted 的基本用法与返回结果**

最基础的排序是对数字或字符串进行升序排列

```
print(sorted([3, 1, 2]))          # [1, 2, 3]
print(sorted(("b", "a", "c")))    # ['a', 'b', 'c']
print(sorted("dbca"))             # ['a', 'b', 'c', 'd']
```

注意，sorted 对字符串返回的是字符列表，而不是拼回字符串，如果你需要字符串，可以再用 ‘’.join。

sorted 不会修改原列表

```
a = [3, 1, 2]
b = sorted(a)
print(a)  # [3, 1, 2]
print(b)  # [1, 2, 3]
```

#### **八、key 参数的意义与常见模式**

key 参数是 sorted 的灵魂。它接收一个函数，sorted 会对每个元素调用一次 key 函数，得到一个“排序键”，然后依据排序键进行排序。key 函数的调用次数是 O(n)，排序整体复杂度通常是 O(n log n)，因此 key 的实现应当尽量轻量。

按字符串长度排序

```
words = ["apple", "a", "banana", "cat"]
print(sorted(words, key=len))  # ['a', 'cat', 'apple', 'banana']
```

忽略大小写排序

```
names = ["bob", "Alice", "carol"]
print(sorted(names, key=str.lower))  # ['Alice', 'bob', 'carol']
```

对字典按 value 排序，常用于统计结果展示

```
d = {"a": 3, "b": 1, "c": 2}
print(sorted(d.items(), key=lambda kv: kv[1]))  # [('b', 1), ('c', 2), ('a', 3)]
```

对对象列表按属性排序

```
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

users = [User("Tom", 20), User("Amy", 18), User("Bob", 20)]
print(sorted(users, key=lambda u: u.age))
```

#### **九、稳定排序与多关键字排序**

Python 的排序是稳定的，所谓稳定是指当两个元素的排序键相等时，它们在排序后的相对顺序与原序列一致。这一性质非常重要，因为它使得多关键字排序可以通过“先按次要键排序，再按主要键排序”来实现。



例如，先按 name 排序，再按 age 排序，这样 age 相同的人会保持 name 的顺序

```
users_sorted = sorted(users, key=lambda u: u.name)
users_sorted = sorted(users_sorted, key=lambda u: u.age)
```

不过更常见也更直接的方法是让 key 返回元组，实现一次性多键排序。元组比较是按从左到右逐字段比较，因此可以自然表达主次关系。

```
print(sorted(users, key=lambda u: (u.age, u.name)))
```

这表示先按 age 排序，age 相同再按 name 排序。

#### **十、reverse 参数与降序排序**

reverse=True 会整体反转排序结果，从升序变为降序

```
print(sorted([1, 3, 2], reverse=True))  # [3, 2, 1]
```

对于按 value 降序排序同样适用

```
print(sorted(d.items(), key=lambda kv: kv[1], reverse=True))
```

需要注意，reverse 作用于排序结果整体，而不是单个字段。如果你需要某个字段升序、另一个字段降序，通常的做法是在 key 中对某个数值字段取负，或者使用更复杂的表达，例如 key 返回 (primary, -secondary) 的模式。

#### **十一、sorted 与 list.sort 的选择建议**

如果你希望保留原数据不变，使用 sorted 更合适，因为它返回新列表。若你处理的是一个列表，并且希望原地排序节省内存开销，使用 list.sort 更合适。两者都支持 key 与 reverse，并且底层排序算法一致，因此性能差异通常来自是否复制列表以及内存分配。

#### **十二、sorted 的复杂度与实际性能特征**

Python 使用的是 TimSort，这是一种针对真实世界数据优化的稳定排序算法。它在一般情况下复杂度为 O(n log n)，但当数据本身部分有序时，性能可能接近 O(n)。这也是为什么在工程实践中，Python 排序通常表现得非常快，并且对“近似有序”的数据有明显优势。

#### **十三、总结与常用落地模式**

defaultdict 适用于需要自动初始化并持续更新的场景，例如计数、分组、去重收集、构建索引和嵌套结构。它的关键机制是 default_factory，缺失键访问会产生副作用并写入默认值。sorted 适用于任意可迭代对象的排序，返回新列表，支持 key 指定排序依据、reverse 控制排序方向，并具备稳定排序性质，从而易于实现多关键字排序。两者都属于 Python 中高频出现的“让代码更短、更稳、更清晰”的工具，但也都需要理解其行为细节，才能在复杂逻辑中避免隐蔽错误。



### python中的tuple元组

#### **一、tuple 的基本定位与核心概念**

tuple 是 Python 中的一种内置数据结构，中文通常称为“元组”。从功能上看，tuple 可以理解为一种只读版本的 list，它用于按顺序存储一组元素，但一旦创建完成，其中的元素就不能被修改。tuple 的设计目标是提供一种轻量、稳定、可哈希的序列类型，因此在很多需要“不可变数据容器”的场景中被广泛使用。tuple 属于序列类型，支持索引、切片、迭代等操作，但不支持任何会改变自身内容的操作。

#### **二、tuple 的创建方式**

tuple 的创建方式非常灵活，最常见的方式是使用圆括号字面量，例如

```
t = (1, 2, 3)
```

圆括号在多数情况下是可选的，只要用逗号分隔多个对象即可形成 tuple，例如

```
t = 1, 2, 3
```

这是 Python 中所谓的“元组打包”。创建空元组需要显式使用括号

```
t = ()
```

创建只有一个元素的元组时必须在元素后加逗号，否则会被当作普通对象处理

```
t = (5,)  
t = 5,
```

如果写成 (5) 则只是一个整数表达式而不是元组。也可以使用 tuple 构造函数从其他可迭代对象创建元组

```
t = tuple([1, 2, 3])
t = tuple("abc")
```

这些方式都会生成新的元组对象。

#### **三、tuple 的不可变性**

tuple 的最核心特性是不可变性。所谓不可变，是指元组一旦创建完成，就不能进行插入、删除或修改元素的操作。以下操作在 tuple 上都是非法的

```
t = (1, 2, 3)
t[0] = 10
t.append(4)
del t[1]
```

这些都会抛出 TypeError。不可变性带来的一个重要好处是稳定性和安全性。因为 tuple 不会被修改，所以可以放心地在函数之间传递，不必担心被意外改变。不可变性还使 tuple 可以作为字典的键或集合的元素，而 list 则不可以。

#### **四、tuple 的索引与切片**

虽然 tuple 不可变，但它完全支持序列读取操作。可以使用下标访问元素

```
t = (10, 20, 30)
print(t[0])
print(t[-1])
```

也可以使用切片操作得到新的元组

```
print(t[1:3])
print(t[:2])
print(t[::-1])
```

这些操作都不会改变原 tuple，而是返回新的 tuple 对象。tuple 还支持 in 运算符进行成员判断

```
if 20 in t:
    print("exists")
```

#### **五、tuple 的常用方法**

tuple 是一个非常精简的类型，只提供两个内置方法。count 方法用于统计某个元素出现的次数

```
t = (1, 2, 2, 3)
print(t.count(2))
```

index 方法用于查找某个元素第一次出现的位置

```
print(t.index(3))
```

如果要查找的元素不存在，index 会抛出 ValueError。由于 tuple 不可变，因此没有 append、insert、remove 等方法。

#### **六、tuple 的打包与解包**

tuple 在 Python 中经常用于打包和解包操作。所谓打包，是指把多个对象组合成一个 tuple

```
t = 1, 2, 3
```

解包则是把 tuple 中的元素一次性赋值给多个变量

```
a, b, c = t
```

这种语法在函数返回多个值时非常常见

```
def f():
    return 1, 2
x, y = f()
```

还可以使用星号表达式进行部分解包

```
t = (1, 2, 3, 4, 5)
a, *b, c = t
```

这种解包机制是 tuple 在实际编程中非常重要的应用场景之一。

#### **七、tuple 与 list 的区别**

tuple 和 list 都是有序序列，但在设计目标上存在本质差异。list 更适合表示“会变化的数据集合”，而 tuple 更适合表示“固定结构的数据记录”。tuple 的优势包括更高的安全性、更低的内存开销以及可以作为哈希键。list 的优势则是灵活可变，适合频繁修改的场景。通常的经验是，如果数据结构在逻辑上不应该被修改，优先选择 tuple。

#### **八、tuple 的哈希特性**

tuple 的不可变性使其具备可哈希性，只要 tuple 中的所有元素本身也是可哈希的，那么整个 tuple 就可以作为字典的键或集合的元素

```
d = {(1, 2): "value"}
s = {(3, 4), (5, 6)}
```

如果 tuple 中包含不可哈希对象，例如列表，则整个 tuple 也变为不可哈希

```
t = ([1, 2], 3)
hash(t)
```

这会抛出 TypeError。可哈希性是 tuple 在很多算法和数据结构中被广泛使用的重要原因。

#### **九、tuple 的性能特点**

由于 tuple 不可变，其内部实现比 list 更简单，通常在以下方面更高效。tuple 的内存占用通常比等价的 list 更小，创建速度更快，访问速度在某些场景下也略优。对于只读数据结构，使用 tuple 可以减少解释器的管理成本，也更容易被优化。很多 Python 内部结构，例如函数参数、返回值、字节码操作，都大量依赖 tuple。

#### **十、tuple 中的可变对象问题**

虽然 tuple 本身不可变，但如果 tuple 中包含可变对象，那么这些对象的内容仍然可以被修改

```
t = ([1, 2], 3)
t[0].append(4)
```

这里 tuple 的结构没有改变，但内部列表的内容发生了变化。这说明 tuple 的不可变性是结构级别的，而不是递归不可变。理解这一点对于避免隐蔽 bug 非常重要。

#### **十一、tuple 的常见使用场景**

tuple 在 Python 中用途非常广泛。它常被用于函数返回多个值、表示数据库记录、表示坐标点或固定结构数据、作为字典键以及作为不可变的配置对象。很多内置 API 也倾向于使用 tuple，例如函数参数列表、异常信息、切片对象等。tuple 由于不可变，更适合作为跨模块或跨线程共享的数据载体。

#### **十二、命名元组 namedtuple 的扩展**

在实际项目中，如果需要同时具备 tuple 的不可变性和更清晰的字段语义，可以使用 collections.namedtuple。它允许通过属性名访问元素

```
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p.x, p.y)
```

namedtuple 本质上仍然是 tuple 的一种扩展形式，但在可读性上更友好。

#### **十三、总结**

tuple 是 Python 中一种轻量、不可变、有序的序列类型。它通过不可变性提供安全性和可哈希性，适合表示固定结构的数据。tuple 支持索引、切片、迭代、打包与解包等操作，但不支持任何修改操作。理解 tuple 的设计理念和行为细节，对于写出高效、稳定、清晰的 Python 代码非常重要。在需要稳定数据结构的场景下，tuple 通常是比 list 更合适的选择。

## 2026-01-19

### python中的set()函数

#### **一、set 的基本概念**

set 是 Python 内置的一种数据结构，中文通常称为“集合”。它的本质是一个**无序、不重复、基于哈希表实现的容器**。与 list 或 tuple 不同，set 中的元素没有位置索引概念，也不会保存插入顺序，其核心目标是快速判断“某个元素是否存在”，以及进行集合运算。set 中的每个元素都必须是可哈希的对象，例如整数、字符串、元组等，而像 list、dict 这样的可变对象不能作为 set 的元素。

#### **二、set 的创建方式**

创建集合最常见的方式是使用花括号字面量：

```
s = {1, 2, 3}
```

如果想创建空集合，必须使用构造函数：

```
s = set()
```

直接写 {} 会创建一个空字典，而不是空集合。也可以通过 set(iterable) 从任意可迭代对象创建集合：

```
s = set([1, 2, 2, 3])
```

由于 set 自动去重，结果会是 {1, 2, 3}。利用这一点，可以非常方便地实现列表去重：

```
unique = list(set([1, 1, 2, 3, 3]))
```

#### **三、set 的基本特性**

set 具有三个最核心的特性：第一是**无序性**，元素在集合中的排列顺序不固定；第二是**唯一性**，同一个值不会重复出现；第三是**高效性**，基于哈希表实现的查找、插入和删除操作在平均情况下时间复杂度为 O(1)。由于这些特性，set 非常适合用于成员判断、去重、集合运算等场景。

#### **四、set 的增删查改操作**

向集合中添加元素使用 add 方法：

```
s.add(10)
```

如果元素已经存在，再次 add 不会产生任何效果。若要一次性添加多个元素，可以使用 update 方法：

```
s.update([1, 2, 3])
```

删除元素有多种方式。remove(x) 会删除元素 x，如果 x 不存在会抛出 KeyError：

```
s.remove(2)
```

discard(x) 也用于删除元素，但如果元素不存在不会报错：

```
s.discard(2)
```

pop() 会随机删除并返回一个元素，因为 set 是无序的，所以 pop 删除的元素无法预测：

```
x = s.pop()
```

clear() 用于清空整个集合：

```
s.clear()
```

成员查询非常高效，使用 in 运算符即可：

```
if 3 in s:
    print("exists")
```

#### **五、set 的集合运算**

set 的最大价值体现在数学意义上的集合运算上，包括并集、交集、差集和对称差等操作。并集运算表示两个集合中所有不同元素的集合，可以使用 | 运算符或 union 方法：

```
a | b
a.union(b)
```

交集运算表示两个集合共有的元素，可以使用 & 或 intersection：

```
a & b
a.intersection(b)
```

差集运算表示属于 a 但不属于 b 的元素，使用 - 或 difference：

```
a - b
a.difference(b)
```

对称差表示属于 a 或 b 但不同时属于两者的元素，使用 ^ 或 symmetric_difference：

```
a ^ b
a.symmetric_difference(b)
```

这些运算都不会修改原集合，而是返回新的集合对象。

#### **六、集合运算的原地版本**

如果希望直接修改原集合而不是生成新集合，可以使用带 update 的版本。并集原地更新：

```
a.update(b)
```

交集原地更新：

```
a.intersection_update(b)
```

差集原地更新：

```
a.difference_update(b)
```

对称差原地更新：

```
a.symmetric_difference_update(b)
```

这些方法会直接改变 a 的内容，在需要节省内存或减少中间对象创建时非常有用。

#### **七、集合关系判断**

set 还支持集合关系的判断操作。判断一个集合是否是另一个集合的子集：

```
a <= b
a.issubset(b)
```

判断是否是超集：

```
a >= b
a.issuperset(b)
```

判断两个集合是否没有交集：

```
a.isdisjoint(b)
```

这些操作在逻辑判断和权限控制等场景中非常常见。

#### **八、set 的遍历与长度**

虽然 set 无序，但仍然可以遍历：

```
for x in s:
    print(x)
```

获取集合中元素个数使用 len(s)，时间复杂度为 O(1)。

#### **九、set 的时间复杂度特点**

由于 set 基于哈希表实现，其核心操作的平均时间复杂度如下：查找 O(1)，插入 O(1)，删除 O(1)，集合运算通常为 O(len(a) + len(b))。这使得 set 在处理大规模数据时比 list 更高效，特别是在频繁进行成员判断时，性能优势非常明显。

#### **十、set 的常见应用场景**

set 在实际编程中用途非常广泛。最典型的是列表去重，通过 set(list) 快速得到不重复元素。成员判断场景中，使用 set 替代 list 可以极大提高效率。集合运算可以方便地处理权限交集、标签匹配、数据过滤等问题。set 还常用于算法题中的“已访问节点记录”，例如图遍历或搜索算法中记录 visited 状态。

#### **十一、不可变集合 frozenset**

普通 set 是可变对象，因此不能作为字典的 key 或另一个 set 的元素。Python 提供了不可变版本 frozenset，它具有与 set 相同的运算能力，但创建后不能修改：

```
fs = frozenset([1, 2, 3])
```

frozenset 可以作为字典键或放入其他 set 中，这在某些复杂数据结构中非常有用。

#### **十二、常见陷阱与注意事项**

创建空集合时必须使用 set() 而不是 {}，这是新手最常见的错误。set 中的元素必须可哈希，尝试将 list 或 dict 放入 set 会报 TypeError。由于 set 无序，不要依赖其遍历顺序。pop 操作删除的是随机元素，不适合用来实现“队列”或“栈”。在大量元素的场景下，set 虽然查询快，但会比 list 占用更多内存，这是空间换时间的典型例子。

#### **十三、与 list 的对比选择**

当需要频繁进行“是否存在”判断时，应优先选择 set 而不是 list。当需要保持顺序或允许重复元素时，应使用 list。当需要既去重又要保持顺序，可以考虑 dict.fromkeys 或 Python 3.7 以后的有序字典特性。set 更适合数学集合运算，而 list 更适合顺序处理和索引访问。

#### **十四、总结**

set 是 Python 中极为重要的数据结构，它通过哈希表实现了高效的去重、查找和集合运算能力。掌握 set 的各种操作方法，可以显著提升代码性能和表达能力。在实际开发中，合理使用 set 往往能把原本复杂的逻辑简化为简洁高效的集合表达式，是 Python 编程中不可或缺的基础工具。

## 2026-01-22

### python常用数据类型的增删改查

#### **一、str（字符串，immutable）**

str 是**不可变的字符序列**，任何“修改”本质上都会创建新对象。

查

可以通过索引、切片、成员判断、方法查询内容

```
s = "hello"
s[0]
s[1:4]
"h" in s
s.find("ll")
s.count("l")
```

增

字符串不能原地增加，只能通过拼接生成新字符串

```
s2 = s + " world"
s3 = "".join([s, " world"])
```

删

不存在真正的删除字符操作，只能通过切片“绕过”

```
s2 = s[:1] + s[2:]
```

改

不能修改单个字符，只能整体替换

```
s2 = s.replace("l", "x")
```

要点

str 的“增删改”全是**新建字符串**，适合只读文本，不适合频繁修改。

#### **二、list（列表，mutable，有序）**

list 是**最灵活、最常用**的可变序列。

查

```
a = [1, 2, 3]
a[0]
a[-1]
a[1:3]
2 in a
len(a)
```

增

```
a.append(4)
a.extend([5, 6])
a.insert(1, 10)
```

删

```
a.pop()
a.pop(1)
a.remove(2)
del a[0]
a.clear()
```

改

```
a[0] = 100
a[1:3] = [7, 8]
```

要点

- append / pop 尾部操作快
- remove 是线性搜索
- 适合顺序数据和频繁修改

#### **三、tuple（元组，immutable，有序）**

tuple 是**不可变列表**，多用于固定结构数据。

查

```
t = (1, 2, 3)
t[0]
t[1:]
2 in t
```

增 / 删 / 改

不支持，所有操作都要新建

```
t2 = t + (4,)
```

要点

- 不可变
- 可作为 dict 的 key
- 常用于函数返回值、结构化记录

#### **四、set（集合，mutable，无序，去重）**

set 是基于哈希表的无序集合，强调“存在性”和“集合运算”。

查

```
s = {1, 2, 3}
2 in s
len(s)
```

增

```
s.add(4)
s.update([5, 6])
```

删

```
s.remove(2)    # 不存在会报错
s.discard(2)   # 不存在不报错
s.pop()        # 随机删除
s.clear()
```

改

集合中元素不可修改，只能删后再加。

要点

- 成员判断 O(1)
- 无序
- 非常适合去重、交并差运算

#### **五、frozenset（不可变集合）**

frozenset 是 set 的不可变版本。

查

```
fs = frozenset([1, 2, 3])
1 in fs
```

增 / 删 / 改

全部不支持，只能生成新对象。

要点

- 可作为 dict key
- 用于“集合本身需要可哈希”的场景

#### **六、dict（字典，mutable，key 唯一）**

dict 是 Python 中**最核心的数据结构**之一，基于哈希表。

查

```
d = {"a": 1, "b": 2}
d["a"]
d.get("c")
"a" in d
d.keys()
d.values()
d.items()
```

增

```
d["c"] = 3
d.update({"d": 4})
```

改

```
d["a"] = 100
```

删

```
del d["a"]
d.pop("b")
d.pop("x", None)
d.clear()
```

要点

- key 必须可哈希
- 查找、插入、删除平均 O(1)
- 3.7+ 保证插入顺序

#### **七、defaultdict（dict 的子类，自动初始化）**

defaultdict 用来**避免“先判断 key 是否存在”的模板代码**。

查

```
from collections import defaultdict
d = defaultdict(list)
d["x"]          # 返回空 list，并写入
```

增 / 改

```
d["a"].append(1)
d["a"].append(2)
```

删

和 dict 完全一致

```
del d["a"]
```

要点

- 访问不存在的 key 会**自动创建**
- 适合统计、分组、聚合
- 不适合“只读查询”

#### **八、Counter（计数器，本质是 dict）**

Counter 是 defaultdict(int) 的语义化版本。

查

```
from collections import Counter
c = Counter("ababc")
c["a"]
```

增 / 改

```
c["a"] += 1
c.update("ccc")
```

删

```
del c["b"]
```

要点

- 专为计数设计
- 可直接做加减、交并操作

#### **九、deque（双端队列）**

deque 适合**头尾高效操作**。

查

```
from collections import deque
q = deque([1, 2, 3])
q[0]
```

增

```
q.append(4)
q.appendleft(0)
```

删

```
q.pop()
q.popleft()
```

改

```
q[1] = 10
```

要点

- 头尾操作 O(1)
- 比 list 更适合队列、滑动窗口

#### **十、bytes / bytearray（二进制数据）**

bytes 是不可变，bytearray 是可变。

查

```
b = b"abc"
b[0]
```

增 / 删 / 改

bytes 不支持

```
ba = bytearray(b"abc")
ba[0] = 100
ba.append(101)
```

要点

- 网络、文件、加密常用
- bytearray 用于原地修改

#### **十一、NoneType**

None 只有一个值：None。

查

```
x is None
```

增 / 删 / 改

不存在

要点

- 表示“无值 / 缺失 / 未初始化”

#### 十二、bool（布尔）**

bool 是 int 的子类。

查

```
True and False
```

增 / 删 / 改

不可变

要点

- True == 1, False == 0
- 主要用于条件判断

#### **十三、数值类型（int / float）**

数值类型是不可变的。

查

```
x + 1
x * 2
```

改

```
x = x + 1
```

要点

- 不可变
- 修改就是重新绑定

#### **十四、一个总览对照表（核心记忆）**

| **类型**    | **是否可变** | **是否有序** | **是否可哈希** | **典型用途** |
| ----------- | ------------ | ------------ | -------------- | ------------ |
| str         | 否           | 是           | 是             | 文本         |
| list        | 是           | 是           | 否             | 顺序数据     |
| tuple       | 否           | 是           | 是             | 结构化记录   |
| set         | 是           | 否           | 否             | 去重、集合   |
| frozenset   | 否           | 否           | 是             | 不可变集合   |
| dict        | 是           | 是           | 否             | 映射         |
| defaultdict | 是           | 是           | 否             | 分组统计     |
| Counter     | 是           | 是           | 否             | 计数         |
| deque       | 是           | 是           | 否             | 队列         |
| bytes       | 否           | 是           | 是             | 二进制       |
| bytearray   | 是           | 是           | 否             | 可变二进制   |



#### **十五、总结性理解**

Python 的数据类型可以从三个维度理解：

第一，**是否可变**（决定能不能原地改）；

第二，**是否有序**（决定能不能用索引、切片）；

第三，**是否基于哈希**（决定查找效率和可否作为 key）。



真正写得好的 Python 代码，往往不是“会用所有类型”，而是**在合适的地方用合适的数据结构**。

### **Python 常用数据类型增删改查关键词总表**

| **数据类型**    | **查（查询/访问）**                          | **增（添加）**                  | **删（删除）**                          | **改（修改）**         |
| --------------- | -------------------------------------------- | ------------------------------- | --------------------------------------- | ---------------------- |
| **str**         | in, [], [:], .find(), .count()               | +, .join()                      | 切片重组                                | .replace()（生成新串） |
| **list**        | in, [], [:], .index()                        | .append(), .extend(), .insert() | .pop(), .remove(), del, .clear()        | []= , [:] =            |
| **tuple**       | in, [], [:], .index(), .count()              | 重新构造 +                      | 不支持                                  | 不支持                 |
| **set**         | in, len()                                    | .add(), .update()               | .remove(), .discard(), .pop(), .clear() | 不支持（删后再加）     |
| **frozenset**   | in, len()                                    | 不支持                          | 不支持                                  | 不支持                 |
| **dict**        | in, [], .get(), .keys(), .values(), .items() | d[k]=v, .update()               | del, .pop(), .clear()                   | d[k]=new_v             |
| **defaultdict** | in, []（自动建值）                           | 自动创建 + 修改                 | del, .pop(), .clear()                   | 同 dict                |
| **Counter**     | [], .get()                                   | +=, .update()                   | del, .subtract()                        | +=, -=                 |
| **deque**       | [], len()                                    | .append(), .appendleft()        | .pop(), .popleft(), .clear()            | []=                    |
| **bytes**       | in, [], [:]                                  | 不支持                          | 不支持                                  | 不支持                 |
| **bytearray**   | in, [], [:]                                  | .append(), .extend()            | .pop(), del, .clear()                   | []=                    |
| **int / float** | 数值运算                                     | 不支持                          | 不支持                                  | 重新赋值               |
| **bool**        | 逻辑运算                                     | 不支持                          | 不支持                                  | 重新赋值               |
| **NoneType**    | is None                                      | 不支持                          | 不支持                                  | 不支持                 |

#### **三个非常重要的速记原则**

1️⃣ **是否可变，决定“能不能原地改”**

- 不可变：str, tuple, int, float, bytes
- 可变：list, set, dict, deque, bytearray

2️⃣ **是否基于哈希，决定是否支持 in 的 O(1) 查询**

- 哈希结构：set, dict, defaultdict, Counter
- 非哈希顺序结构：list, tuple, deque

3️⃣ **in 的语义不同**

- list / tuple：线性查找
- set / dict：哈希查找
- dict 中：in 查的是 **key**

#### **一个极简“记忆版”**

- **顺序 + 可改** → list
- **顺序 + 不可改** → tuple / str
- **去重 + 查快** → set
- **键值映射** → dict
- **统计计数** → Counter
- **自动初始化映射** → defaultdict
- **队列 / 双端** → deque

### Python中的Counter

#### **一、Counter 的本质与定位**

Counter 位于 collections 模块中，是 **dict 的一个子类**，专门用于“计数”场景。它的核心语义是：

**key 表示元素，value 表示该元素出现的次数（计数值，整数）**。

从数据结构角度看，Counter 并没有引入新的底层机制，它仍然是基于哈希表实现的映射结构；从语义角度看，它对“计数”这一高频模式进行了标准化和增强。

换句话说，Counter 可以被理解为：

一个“自带计数语义和集合运算能力的字典”。

#### **二、Counter 的创建方式**

最常见的创建方式是直接从可迭代对象构造：

```
from collections import Counter

c = Counter("ababc")
```

此时结果等价于：

```
{'a': 2, 'b': 2, 'c': 1}
```

也可以从列表、元组等构造：

```
Counter([1, 2, 2, 3])
```

可以从普通字典构造（视作初始计数）：

```
Counter({"a": 2, "b": 1})
```

还可以创建空 Counter：

```
Counter()
```

需要注意的是，**Counter 并不会限制 value 为非负数**，它允许 0 和负数存在，这一点在后续运算中非常重要。

#### **三、Counter 的“查”操作**

作为 dict 的子类，Counter 支持所有常规的查询方式。

使用下标访问：

```
c["a"]
```

如果 key 不存在，**不会抛出 KeyError，而是返回 0**，这是 Counter 与 dict 的一个关键差异。

```
c["not_exist"]   # 返回 0
```

也可以使用 get：

```
c.get("a", 0)
```

成员判断：

```
"a" in c
```

注意：

in 判断的是 key 是否存在，而不是计数是否大于 0。如果某个 key 的计数是 0，但仍在 Counter 中，那么 in 仍然返回 True。

#### **四、Counter 的“增”与“改”操作**

Counter 的核心操作就是“累加计数”。

最直接的方式是使用加法：

```
c["a"] += 1
c["b"] += 3
```

即使 key 原本不存在，也不会报错，因为不存在的 key 默认计数是 0。

可以批量更新：

```
c.update("abc")
c.update([1, 2, 2])
```

update 的语义是“加法更新”，而不是覆盖：

```
Counter("ab").update("a")
```

结果中 "a" 的计数会增加 1，而不是被替换。

#### **五、Counter 的“删”操作**

可以像 dict 一样使用 del：

```
del c["a"]
```

也可以手动把计数减到 0 或负数：

```
c["a"] -= 2
```

需要注意的是：

**Counter 不会自动删除计数为 0 或负数的 key**。

如果你希望清理这些元素，需要手动处理，例如：

```
c += Counter()   # 会移除计数 <= 0 的 key
```

这是一个常见但不直观的技巧。

#### **六、Counter 的核心增强能力：计数运算**

这是 Counter 相比 dict 最大的价值所在。

##### **1. 加法（合并计数）**

```
c1 = Counter("ab")
c2 = Counter("bc")

c1 + c2 # Counter({'b': 2, 'a': 1, 'c': 1})
```

结果是逐 key 相加，并且 **只保留正计数**。

##### **2. 减法（差分计数）**

```
c1 - c2 # Counter({'a': 1})
```

结果是逐 key 相减，同样只保留正计数。

##### **3. 交集（取最小值）**

```
c1 & c2 # Counter({'b': 1})
```

表示每个 key 的计数取 min。

##### **4. 并集（取最大值）**

```
c1 | c2 # Counter({'a': 1, 'b': 1, 'c': 1})
```

表示每个 key 的计数取 max。

这些运算使 Counter 在“多重集合（multiset）”语义下非常强大。

#### **七、最常用的高级接口**

##### **most_common**

用于返回计数最多的元素：

```
c = Counter([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5])
c.most_common(3) # [(5, 5), (4, 4), (3, 3)]
```

返回一个按计数降序排列的 (key, count) 列表。

##### **elements**

将 Counter 还原为“元素流”：

```
list(c.elements()) # [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
```

每个元素会重复出现 count 次（忽略 count <= 0 的元素）。

#### **八、Counter 与 defaultdict(int) 的区别**

虽然二者都能用于计数，但设计目标不同。

defaultdict(int)：

- 是“自动初始化为 0 的字典”
- 不理解“计数”语义
- 没有集合运算能力

Counter：

- 明确的“计数器”语义
- 不存在 key 时返回 0
- 支持加减、交并、排序、提取 top-k

可以认为：

**defaultdict(int) 是工具，Counter 是模型化抽象。**

#### **九、Counter 的时间复杂度特性**

由于底层仍是哈希表：

- 查询、更新单个元素：平均 O(1)
- update：O(n)
- most_common：O(n log n)（内部排序）

因此 Counter 非常适合中等到较大规模的统计任务。

#### **十、常见应用场景**

Counter 最典型的使用场景包括：

- 词频统计
- 日志事件统计
- 标签出现次数统计
- 多重集合操作
- Top-K 频率分析

在算法题中，Counter 常用于“频率对齐”“元素消耗”“可重集合比较”等问题。

#### **十一、容易踩的坑与注意事项**

第一，不要忘记 Counter 允许负数和 0，这可能导致逻辑错误。

第二，in 只判断 key 是否存在，不判断计数是否大于 0。

第三，update 是加法而不是赋值，和 dict.update 的语义不同。

第四，Counter 的加减运算会自动丢弃非正计数，而直接赋值不会。

#### **十二、总结**

Counter 是 Python 中一个高度工程化的数据结构，用于解决“计数”这一极其常见的问题。它在 dict 的基础上引入了清晰的计数语义、默认 0 行为以及多重集合运算能力，使得原本冗长、易错的计数逻辑变得简洁、可组合、可推理。理解 Counter 的行为边界与运算规则，可以显著提升代码的表达力与可靠性。

## 2026-01-24

### python中的队列

#### **一、什么是队列（Queue）的核心抽象**

队列是一种**先进先出（FIFO, First-In First-Out）的数据结构，其基本约束是：元素只能从队尾进入（入队），只能从队头移除（出队）。最早进入队列的元素，最先被取出。队列的核心价值在于顺序性与公平性**，在任务调度、消息传递、缓冲区管理等场景中非常常见。与栈（LIFO）不同，队列强调的是“先来先服务”。

#### **二、Python 中“队列”的多种实现方式总览**

Python 并没有一个唯一的“队列类型”，而是根据使用场景提供了多种实现方案。最常见的有四类：使用 list 模拟队列、使用 collections.deque、使用 queue.Queue（线程安全）、使用 asyncio.Queue（异步场景）。它们在操作方式、性能特征和适用场景上有明显差异，理解这些差异比记 API 更重要。

#### **三、使用 list 实现队列（不推荐用于高频出队）**

list 是最直观但也是最容易误用的队列实现。其典型做法是：尾部 append 入队，头部 pop(0) 出队。操作方式如下：

```
q = []
q.append(1)
q.append(2)
x = q.pop(0)
```

入队 append 的时间复杂度是 O(1)，但出队 pop(0) 的时间复杂度是 O(n)，因为所有后续元素都需要整体前移。因此，当队列规模较大或出队操作频繁时，list 会产生明显性能问题。list 更适合“偶尔当队列用”的轻量场景，不适合严肃的队列需求。

#### **四、collections.deque：Python 中最常用的队列实现**

deque（double-ended queue，双端队列）位于 collections 模块中，是 Python 官方为队列和双端操作优化的数据结构。deque 底层并非连续数组，而是块状链表结构，因此在两端的插入和删除操作都具有 O(1) 时间复杂度。

基本创建与查询操作如下：

```
from collections import deque
q = deque()
len(q)
```

入队与出队操作：

```
q.append(1)       # 右端入队
q.append(2)
x = q.popleft()   # 左端出队
```

deque 还支持反向操作，使其既能作为队列也能作为栈：

```
q.appendleft(0)
q.pop()
```

deque 支持索引访问（q[0]），但这是 O(n) 操作，因此不应将 deque 当作随机访问容器使用。deque 的核心优势在于：高效、语义明确、线程安全性由调用方控制，是**单线程或轻量并发场景下的首选队列结构**。

#### **五、queue.Queue：线程安全队列**

queue.Queue 位于 queue 模块中，是为**多线程环境**设计的队列实现。它在内部通过锁机制保证并发安全，并提供阻塞式的入队和出队接口。创建方式如下：

```
from queue import Queue
q = Queue(maxsize=10)
```

基本操作：

```
q.put(item)        # 入队，队列满时阻塞
x = q.get()        # 出队，队列空时阻塞
```

附加的控制方法：

```
q.put_nowait(item)
q.get_nowait()
q.empty()
q.full()
q.qsize()
```

queue.Queue 的一个重要特性是**生产者-消费者模型支持**，它常与多线程配合使用，例如任务队列、工作池。需要注意的是，queue.Queue 不支持索引访问，也不暴露底层存储结构，其设计目标是“安全而非灵活”。

#### **六、asyncio.Queue：异步队列**

asyncio.Queue 是为 Python 的异步编程模型（async/await）设计的队列，用于协程之间的通信。其 API 风格与 queue.Queue 类似，但所有阻塞操作都变成了 await 形式。基本使用方式如下：

```
import asyncio
q = asyncio.Queue()
await q.put(item)
x = await q.get()
```

asyncio.Queue 的核心作用是在事件循环中协调生产者与消费者协程，它不会使用线程锁，而是依赖事件循环调度，因此只适用于异步上下文。

#### **七、队列的核心操作语义总结（增删改查）**

从抽象角度看，所有队列都围绕四类操作展开。

查：查看队列长度（len / qsize），判断是否为空（len==0 / empty），但通常不支持随机访问。

增：入队操作（append / put），语义是“加入队尾”。

删：出队操作（popleft / get），语义是“移除队头”。

改：严格意义上的队列不支持中间修改元素，若需要修改，说明该结构可能并不适合用队列建模。

队列的设计哲学是**限制操作能力以换取行为确定性**。

#### **八、不同队列实现的性能与适用场景对比**

list：入队快，出队慢，仅适合极小规模或教学示例。

deque：入队出队都快，API 简洁，是最常用的通用队列实现。

queue.Queue：线程安全，支持阻塞，适合多线程任务调度。

asyncio.Queue：协程安全，适合异步程序，不可用于普通同步代码。

选择队列实现时，首先要问的是：是否需要线程/协程安全，其次才是性能与功能。

#### **九、队列在实际编程中的典型应用**

队列广泛用于广度优先搜索（BFS）、生产者-消费者模型、任务调度系统、消息缓冲、IO 管道、并发任务池等场景。在这些问题中，FIFO 顺序不是“实现细节”，而是问题语义本身的一部分，因此使用队列能够让代码结构更贴合问题模型。

#### **十、常见误区与注意事项**

第一，不要用 list 的 pop(0) 实现高频出队，这是性能陷阱。第二，不要在需要线程安全的场景中直接使用 deque 或 list。第三，如果你频繁想“查看或修改队列中间的元素”，说明你真正需要的可能不是队列，而是 list、heap 或其他数据结构。第四，队列的“简单”来自于操作受限，滥用会破坏这种简洁性。

#### **十一、总结**

Python 中的队列不是单一类型，而是一组围绕 FIFO 抽象构建的数据结构与工具。deque 是最通用、最推荐的同步队列实现；queue.Queue 是并发场景下的安全选择；asyncio.Queue 服务于异步编程模型。理解队列的操作边界与适用场景，能够帮助你在算法设计与工程实践中做出更合理的数据结构选择，从而写出更清晰、更高效的代码。

## 2026-02-04

### python中自带的二分查找

#### **1. 它们是什么：在“已排序序列”里做二分插入定位**

bisect_left / bisect_right 都来自 Python 标准库 bisect，用于在**保持序列有序**的前提下，给定目标值 x，返回它在有序序列 a 中应插入的位置 i（索引），使得插入后仍然有序；它们的区别只在于：遇到“相等元素”时插到**左边**还是**右边**。重要前提：a 必须按升序排列（除非你自己实现降序逻辑），否则结果不可靠。

- bisect_left(a, x, lo=0, hi=len(a))：返回最左插入点 i，满足：a[:i] 中所有元素都 < x，a[i:] 中所有元素都 >= x；等价不等式（在区间 [lo, hi) 上）：a[i-1] < x <= a[i]（边界处按存在性理解）。

- bisect_right(a, x, lo=0, hi=len(a))（别名 bisect(a, x, ...)）：返回最右插入点 i，满足：a[:i] 中所有元素都 <= x，a[i:] 中所有元素都 > x；等价不等式：a[i-1] <= x < a[i]。

  这两个函数都只返回“位置”，不负责插入；若要插入，用 insort_left/insort_right（内部也是二分定位 + list.insert）。

#### **2. 最核心的差异：相等元素的“稳定边界”**

设有序数组 a，目标 x，记 L = bisect_left(a, x)，R = bisect_right(a, x)，那么：a[L:R] 恰好是所有等于 x 的元素（可能为空）；因此 R - L 就是 x 出现次数。

用一个例子直观感受：

```python
from bisect import bisect_left, bisect_right
a = [1, 2, 2, 2, 4, 7]
print(bisect_left(a, 2))   # 1
print(bisect_right(a, 2))  # 4
# a[1:4] == [2,2,2]
```

再看“插入后顺序”：

```python
from bisect import bisect_left, bisect_right
a = [1,2,2,2,4]
x = 2
i1 = bisect_left(a, x)
i2 = bisect_right(a, x)
print(i1, i2)  # 1 4
# 若插到 i1：新2会排在所有2之前
# 若插到 i2：新2会排在所有2之后
```

#### **3. 形式化条件与区间语义（非常重要，避免 off-by-one）**

它们都支持 lo 与 hi，表示只在半开区间 [lo, hi) 上做二分；返回值 i 也必然在 [lo, hi]（注意右端是 hi 而不是 hi-1，因为“插入点”可能在末尾）。形式化地：

- i = bisect_left(a, x, lo, hi) 满足：对所有 j in [lo, i)，有 a[j] < x；对所有 j in [i, hi)，有 a[j] >= x。

- i = bisect_right(a, x, lo, hi) 满足：对所有 j in [lo, i)，有 a[j] <= x；对所有 j in [i, hi)，有 a[j] > x。

  边界情况：若 x 小于区间内最小值，两个函数都返回 lo；若 x 大于区间内最大值，两个函数都返回 hi；若区间为空（lo == hi），返回 lo。

#### **4. 时间复杂度与适用数据结构**

- 定位（bisect_left/right）是二分：比较次数 O(log n)；对 Python list 来说随机访问是 O(1)，所以定位很快。
- 但若你随后真的插入到 list（list.insert 或 insort_*），需要移动元素，整体插入成本是 O(n)；所以 bisect 适合“**只查询位置**”或“**查询频繁、插入不频繁**”的场景；若要大量动态插入并维持有序，通常考虑 bisect + array/deque（仍要搬移）、或第三方结构（如 sortedcontainers）等。

#### **5. 常用技巧与典型用法（带可直接复用的模板）**

**5.1 找“是否存在”与“第一次出现的位置”**：已排序 a，判断 x 是否存在：先求 i = bisect_left(a, x)，再检查 i < len(a) and a[i] == x。

```python
from bisect import bisect_left
def contains(a, x):
    i = bisect_left(a, x)
    return i < len(a) and a[i] == x
```

**5.2 统计出现次数**：count = bisect_right(a, x) - bisect_left(a, x)。

```python
from bisect import bisect_left, bisect_right
def count_x(a, x):
    return bisect_right(a, x) - bisect_left(a, x)
```

**5.3 获取等值区间 [L, R)**：直接得到所有 x 的切片范围。

```python
from bisect import bisect_left, bisect_right
def equal_range(a, x):
    L = bisect_left(a, x)
    R = bisect_right(a, x)
    return L, R  # a[L:R] 全是 x
```

**5.4 lower_bound / upper_bound（算法竞赛同款）**：C++ 里的 lower_bound≈bisect_left，upper_bound≈bisect_right；很多“找第一个 >=x”或“第一个 >x”的问题直接套用。

**5.5 找“最后一个 <= x”的索引**：这类题常见，但注意边界；做法是 i = bisect_right(a, x) - 1，再判断 i >= 0。

```python
from bisect import bisect_right
def last_leq(a, x):
    i = bisect_right(a, x) - 1
    return i if i >= 0 else None
```

**5.6 找“第一个 >= x”的索引**：就是 bisect_left(a, x)；找“第一个 > x”就是 bisect_right(a, x)。

**5.7 用于阈值分桶（bucket）/区间映射**：给定有序分割点 cuts（如分数线、时间段边界），要把值 v 放入哪个桶，常用 bisect_right：返回的索引就是桶编号（取决于你如何定义区间闭开）。

```python
from bisect import bisect_right
cuts = [60, 70, 80, 90]  # 分割点
def grade_bucket(score):
    # 约定：( -inf,60], (60,70], (70,80], (80,90], (90,inf)
    return bisect_right(cuts, score)
```

如果你想要区间形如 [cut_i, cut_{i+1})（左闭右开），一般用 bisect_left 更自然；关键是你要明确“边界包含谁”，再选 left/right。

#### **6. insort_left / insort_right：真正插入（但插入是 O(n)）**

```
from bisect import insort_left, insort_right
a = [1,2,2,4]
insort_left(a, 2)   # 插到所有2之前
# a == [1,2,2,2,4]
insort_right(a, 2)  # 插到所有2之后
# a == [1,2,2,2,2,4]
```

内部逻辑就是：i = bisect_left/right(...) 然后 a.insert(i, x)；所以定位快，但搬移慢。

#### **7. “自定义 key”怎么办：bisect 本身不带 key，常见替代方案**

标准库 bisectht 不接受 key= 参数；如果你要在“按某个字段排序”的对象列表上二分，有两种主流做法：**(A) 用平行 key 数组二分** 或 **(B) 用元组让 Python 比较**。

**7.1 平行 key 数组（最清晰）**：维护 keys = [obj.k for obj in objs] 与 objs 同步；二分在 keys 上定位，再对 objs 做同位置操作。

```python
from bisect import bisect_left
objs = [{"k": 10}, {"k": 20}, {"k": 20}, {"k": 35}]
keys = [o["k"] for o in objs]
x = 20
i = bisect_left(keys, x)  # 1
```

**7.2 用元组比较（常用于“稳定左/右边界”）**：若对象可映射为 (key, tie_breaker)，可把列表存为元组序列并保持排序，然后 bisect 直接对元组做字典序比较；比如要找 key==20 的区间：左边界用 (20, -inf)，右边界用 (20, +inf)（实际用能覆盖范围的哨兵值）。

```python
from bisect import bisect_left, bisect_right
pairs = [(10,"a"), (20,"b"), (20,"c"), (35,"d")]  # 按 (key, second) 排序
L = bisect_left(pairs, (20, ""))      # "" 作为很小的 second（取决于数据域）
R = bisect_right(pairs, (20, chr(0x10FFFF)))  # 作为很大的 second
```

注意：哨兵要与第二维类型可比且能保证上下界；如果第二维不是字符串而是数字，就用极小/极大数。

#### **8. 亲手实现一版：用不变量理解 bisect（理解它为什么对）**

理解 bisect 的关键是“维护不变量（invariant）”：在循环过程中保持一个区间 [lo, hi)，保证插入点一定在其中；每次取 mid 缩小区间直到 lo == hi。bisect_left 选择条件 a[mid] < x 决定往右，否则往左；bisect_right 选择条件 a[mid] <= x 决定往右，否则往左；这正是“相等时偏左/偏右”的根源。

```python
def my_bisect_left(a, x, lo=0, hi=None):
    if hi is None: hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def my_bisect_right(a, x, lo=0, hi=None):
    if hi is None: hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

你可以看到它们只差一个符号：< vs <=；也正因为这个符号，left 会把等于 x 的元素归入右侧（从而插到最左），right 会把等于 x 的元素归入左侧（从而插到最右）。

#### **9. 易错点清单（高频坑位）**

- 没排序就 bisect：结果可能“看似合理但不对”，属于隐蔽 bug；必须保证升序排序一致。
- hi 是“右开”而不是包含端点：hi=len(a) 表示可以插在末尾；很多 off-by-one 都出在这里。
- 想找“最后一个 <=x”却用了 bisect_left：正确是 bisect_right(a,x)-1，并处理空结果（返回 -1 时要小心）。
- 对对象列表二分时忘了 key：bisect 不会帮你按字段比较；需要平行 key 或元组技巧。
- 浮点数比较边界：如果数据来自计算误差，== 或边界插入可能表现不符合直觉；必要时先做容差处理或用 decimal。

bisect_left 和 bisect_right 位于 Python 标准库 bisect 模块中，用于在**已排序序列**中通过**二分查找**快速定位某个元素的插入位置。它们不负责排序，也不直接修改原序列，而是回答一个问题：如果把元素 x 插入到当前有序序列中，插在什么位置才能保持序列仍然有序。其核心价值在于将查找复杂度从线性扫描的 O(n) 降低为 O(log n)，这是在有序数据上进行区间统计、边界定位、频率计算的基础工具。

#### **二、bisect_left 与 bisect_right 的形式化定义**

设有一个升序排列的序列 a，长度为 n，要查找元素 x。

bisect_left(a, x) 返回最小的索引 i，使得对所有 j < i 有 a[j] < x，并且对所有 j ≥ i 有 a[j] ≥ x，即**第一个大于等于 x 的位置**。

bisect_right(a, x) 返回最小的索引 i，使得对所有 j < i 有 a[j] ≤ x，并且对所有 j ≥ i 有 a[j] > x，即**第一个严格大于 x 的位置**。

因此，当 x 在序列中存在重复元素时，left 指向重复区间的左边界，right 指向重复区间的右边界。

#### **三、最直观的行为示例**

假设有序列表 a = [1, 3, 3, 3, 5, 7]。

对 x = 3：

bisect_left(a, 3) 返回 1，对应第一个 3 的位置；

bisect_right(a, 3) 返回 4，对应最后一个 3 的后一个位置。

这两个结果共同刻画了值为 3 的元素在序列中的“闭区间 [1, 4)”范围。

#### **四、核心操作语义（查、增的关系）**

从抽象角度看，bisect 系列函数本质上只做“查”，即查找插入位置，而不直接“增”。如果你真的想插入元素，需要配合列表的插入操作：

使用 a.insert(bisect_left(a, x), x) 可以把 x 插入到重复元素之前；

使用 a.insert(bisect_right(a, x), x) 可以把 x 插入到重复元素之后。

标准库中还提供了 insort_left 和 insort_right，它们是“查找 + 插入”的封装，但底层仍然依赖 bisect_left / bisect_right。

#### **五、通过 bisect 进行“值区间统计”**

bisect 的一个非常重要用途是**在有序数组中统计某个值或某个区间内的元素个数**。

如果要统计值等于 x 的元素个数，可以计算

count = bisect_right(a, x) − bisect_left(a, x)。

如果要统计区间 [L, R] 内的元素个数，可以计算

left = bisect_left(a, L)，right = bisect_right(a, R)，区间长度为 right − left。

这类操作在频率分析、日志时间窗口统计、分桶统计中非常常见。

#### **六、bisect 的 key 参数缺失与设计取舍**

与 sorted 不同，bisect 并不支持 key 参数，这意味着它只能直接对“可比较的原始值”进行二分查找。如果你需要按对象的某个字段进行二分定位，通常的做法是先构造一个“投影数组”，例如把对象列表映射为一个字段值列表，再对该列表使用 bisect。这一设计体现了 bisect 的定位：它是一个底层、高性能、语义简单的工具，而不是高层抽象。

#### **七、时间复杂度与性能边界**

bisect_left 和 bisect_right 的查找时间复杂度为 O(log n)，这是它们的核心优势。但需要注意，如果你在列表上执行插入操作，list.insert 本身是 O(n) 的，因为需要移动后续元素。因此，bisect 非常适合“查边界、算数量”，但不适合在大规模列表上频繁插入。如果你的场景是大量插入并保持有序，通常需要考虑其他数据结构（如平衡树、堆或第三方库）。

#### **八、常见误区与注意事项**

第一，bisect 只对**已排序序列**有意义，如果序列无序，返回值在语义上是错误的，但程序不会报错。第二，bisect 只保证返回一个合法的插入位置，不保证该位置上的元素等于目标值。第三，bisect_left 与 bisect_right 的差异只在“等于 x 的处理方式”，这一点在处理重复元素时至关重要。第四，bisect 操作本身不会修改原序列，任何修改行为都需要显式调用 insert 或 insort

#### **九、与线性搜索的对比理解**

如果你在一个有序数组中，用 for 循环查找第一个 ≥ x 的位置，时间复杂度是 O(n)；使用 bisect_left，则是 O(log n)。当数据规模增大时，这种差异会非常明显。因此，**一旦数据是有序的，边界查找应优先考虑 bisect，而不是手写线性扫描**。

#### **十、总结**

bisect_left 和 bisect_right 是 Python 中用于有序序列的基础级工具，它们通过二分查找精确刻画元素的插入边界。left 定位“第一个不小于 x 的位置”，right 定位“第一个大于 x 的位置”，二者共同定义了重复元素的区间范围。它们广泛用于频率统计、区间查询、阈值分割等场景，是理解和利用“有序数据结构”的关键工具之一。

## 2026-02-05

### python中的zip

#### **1. zip 是什么：把多个可迭代对象“按位置配对”成元组序列**

zip(*iterables, strict=False) 会并行遍历多个可迭代对象（iterable），每次各取出一个元素，组成一个元组 (a_i, b_i, c_i, ...)，不断产出这些元组，直到停止；在 Python 3 中，zip 返回的是**惰性迭代器**（iterator），需要用 list(zip(...))、循环、或再次迭代消费。最常见的理解是“列对齐→按行打包”，如果把每个 iterable 看作一列，那么 zip 生成的就是一行行的记录。最基础用法：zip([1,2,3], ['a','b','c']) -> (1,'a'), (2,'b'), (3,'c')。

```
a = [1, 2, 3]
b = ["x", "y", "z"]
for pair in zip(a, b):
    print(pair)  # (1,'x'), (2,'y'), (3,'z')
```

#### **2. 核心语义：长度/维度不一致时怎么办（默认：截断到最短）**

**2.1 “维度不一致”在 zip 里通常指“长度不一致”**：比如两个列表一个长 5 一个长 3；默认行为是**以最短的为准**，迭代到某一个 iterable 耗尽就停止，剩余更长 iterable 的元素会被忽略。

设各 iterable 长度为 n1, n2, ..., nk，则 zip 产出条数为：m = min(n1, n2, ..., nk)。

```
a = [1, 2, 3, 4]
b = ["a", "b"]
print(list(zip(a, b)))  # [(1,'a'), (2,'b')]  后面的 3,4 被丢弃
```

**2.2 strict=True：要求长度完全一致，否则报错**：从 Python 3.10 起，zip(..., strict=True) 会在发现某个 iterable 提前结束时抛出 ValueError，用于“我必须保证每列对齐”的数据处理场景，避免静默截断导致数据错位。

```
a = [1, 2, 3, 4]
b = ["a", "b"]
try:
    list(zip(a, b, strict=True))
except ValueError as e:
    print("ValueError:", e)
```

**2.3 想要“按最长对齐并填充缺失值”怎么办：用 itertools.zip_longest**：标准库 itertools.zip_longest(*iterables, fillvalue=...) 会以最长为准，短的用 fillvalue 补齐。

```
from itertools import zip_longest
a = [1, 2, 3, 4]
b = ["a", "b"]
print(list(zip_longest(a, b, fillvalue=None)))
# [(1,'a'), (2,'b'), (3,None), (4,None)]
```

#### **3. 数据类型不一致时怎么办：zip 不做类型转换，只做“打包”**

**3.1 zip 不关心元素类型，只要可迭代就行**：不同 iterable 的元素可以是任意类型，zip 只是把同位置元素放进同一个元组里；因此“数据类型不一致”不会导致 zip 本身报错。

```
a = [1, 2, 3]                    # int
b = ["x", "y", "z"]              # str
c = [{"k":1}, {"k":2}, {"k":3}]  # dict
print(list(zip(a, b, c)))
# [(1,'x',{'k':1}), (2,'y',{'k':2}), (3,'z',{'k':3})]
```

**3.2 但要注意：后续对打包结果做运算时可能类型错误**：比如你把 (int, str) 当作能相加；zip 不负责保证可运算性。

```
pairs = list(zip([1,2,3], ["10","20","30"]))
# 你若直接做 1 + "10" 会 TypeError，需要显式转换
nums = [x + int(y) for x, y in pairs]  # [11,22,33]
```

**3.3 iterable 的“数据结构类型”不一致也没关系**：list、tuple、set、dict、generator、string 都能混用，但注意它们的迭代规则不同：字符串按字符迭代；字典默认迭代的是 key；集合无序导致配对不稳定。

```
print(list(zip([1,2,3], (10,20,30))))          # list + tuple OK
print(list(zip([1,2,3], "abc")))               # "abc" -> 'a','b','c'
print(list(zip([1,2,3], {"k1":9,"k2":8,"k3":7})))  # dict -> keys
print(list(zip([1,2,3], {100,200,300})))       # set 无序，结果顺序不保证
```

处理字典时想按 value 或 items：

```
d = {"k1": 9, "k2": 8, "k3": 7}
print(list(zip([1,2,3], d.values())))  # values
print(list(zip([1,2,3], d.items())))   # items: ('k1',9)...
```

#### **4. “维度不一致”的更深层：元素本身是向量/矩阵时如何理解 zip 的配对层级**

很多人说“维度不一致”，其实包含两层意思：外层长度不一致（zip 的停止条件），内层元素是序列/数组，其形状可能不一致（zip 不会管，只会把它们当作普通元素打包）。

**4.1 外层长度一致，但内层形状不一致：zip 仍然正常**：

```
xs = [[1,2,3], [4,5], [6]]   # 内层长度 3,2,1
ys = ["A", "B", "C"]
print(list(zip(xs, ys)))
# [([1,2,3],'A'), ([4,5],'B'), ([6],'C')]
```

这里 zip 完全不关心 [1,2,3] 和 [4,5] 的“维度”，它们只是两个对象。

**4.2 你想“逐元素配对内层”时，需要嵌套 zip 或先对齐内层**：

例如把二维“按列对齐”转置：

```
mat = [
    [1, 2, 3],
    [4, 5, 6],
]
print(list(zip(*mat)))  # [(1,4), (2,5), (3,6)]  转置（行->列）
```

但如果内层长度不一致，zip(*mat) 默认会截断到最短内层：

```
ragged = [
    [1, 2, 3],
    [4, 5],
    [6],
]
print(list(zip(*ragged)))  # [(1,4,6)]  只保留第0列
```

想保留所有列并填充缺失：

```
from itertools import zip_longest
print(list(zip_longest(*ragged, fillvalue=None)))
# [(1,4,6), (2,5,None), (3,None,None)]
```

#### **5. zip 与“解包 \*”的组合：转置、反转、重组（但要小心可重复迭代性）**

**5.1 zip(\*iterables) 常用于“解包后转置”**：上面矩阵转置就是经典例子。

**5.2 反向 unzip：把 zip 的结果拆回多列**：

```
pairs = [(1,"a"), (2,"b"), (3,"c")]
xs, ys = zip(*pairs)
print(xs)  # (1,2,3)
print(ys)  # ('a','b','c')
```

注意：zip(*pairs) 要求 pairs 非空；空会报 ValueError: not enough values to unpack，更稳健写法：

```
pairs = []
xs, ys = zip(*pairs) if pairs else ((), ())
```

**5.3 zip 的输入是迭代器/生成器时，只能消费一次**：

```
g = (i*i for i in range(3))
z = zip(g, ["a","b","c"])
print(list(z))  # 第一次消费 OK
print(list(z))  # 第二次为空，因为 zip 迭代器已耗尽
```

#### **6. 与“数据维度/长度不一致”相关的工程处理模式（非常常用）**

**6.1 数据表对齐：要求长度一致就用 strict=True**：例如训练数据 (texts, labels) 必须一一对应，否则直接报错比静默截断安全。

```
def make_records(texts, labels):
    return list(zip(texts, labels, strict=True))
```

**6.2 流式数据：一边读一边 zip（惰性）**：zip 不会把所有数据读进内存，适合大文件逐行配对，但依旧会受最短流的结束影响。

```
def line_pairs(f1, f2):
    for l1, l2 in zip(f1, f2):
        yield l1.rstrip("\n"), l2.rstrip("\n")
```

**6.3 不同长度要保留全部：zip_longest + 后处理**：比如有缺失标签/缺失特征要填默认值或跳过。

```
from itertools import zip_longest
def align_longest(a, b, fill=None):
    for x, y in zip_longest(a, b, fillvalue=fill):
        yield x, y
```

**6.4 只想截断但要显式：先取最短长度 min_len 再切片**：比隐式截断更可读，尤其在审计代码时。

```
a = [1,2,3,4]
b = ["a","b"]
m = min(len(a), len(b))
pairs = list(zip(a[:m], b[:m]))
```

#### **7. 常见坑与细节（和“类型/维度不一致”强相关）**

- 字典：zip(d1, d2) 默认配对的是 key，而且两个 dict 的 key 集不一定一致；如果你要按相同 key 对齐，应先对 key 取交集或统一排序：

```
d1 = {"a":1,"b":2}
d2 = {"a":10,"c":30}
common = sorted(d1.keys() & d2.keys())
pairs = [(k, d1[k], d2[k]) for k in common]  # [('a',1,10)]
```

- 集合：无序导致每次运行配对结果顺序可能不同，不适合需要稳定对齐的数据处理；若必须用，先排序：zip(sorted(s1), sorted(s2))。
- 字符串：按字符迭代，经常不是你想要的“单个字符串作为一个元素”；若要把整个字符串当一个元素，包一层：zip([s], other) 或 (s,)。
- 内层不齐的二维数据：zip(*rows) 会截断到最短行；想保留列用 zip_longest(*rows)。
- 惰性迭代：zip 结果如果要复用，必须保存为 list/tuple；否则第二次迭代为空。
- strict=True 的版本要求：若运行环境 <3.10，则没有 strict 参数；这时可手动检测长度或使用 itertools.zip_longest 检测是否有填充值出现来模拟一致性检查。

#### **8. 用一个综合例子串起来：类型不一致 + 长度不一致 + 内层维度不一致**

目标：把 ids、texts、embeddings 对齐成记录；其中 ids 是 int 列表，texts 是字符串列表，embeddings 是不规则向量（内层长度可能不同），而且 texts 缺一条。

```
from itertools import zip_longest
ids = [101, 102, 103, 104]
texts = ["q1", "q2", "q3"]                 # 少一个
embs = [[0.1,0.2], [0.3,0.4,0.5], [0.6], [0.7,0.8]]  # 内层不齐但无所谓
records = []
for i, t, e in zip_longest(ids, texts, embs, fillvalue=None):
    # zip_longest 保证 ids 的最后一条不会丢；t 缺失时为 None
    records.append({"id": i, "text": t, "emb": e, "emb_dim": None if e is None else len(e)})
print(records)
```

这里展示了三点：外层长度不一致用 zip_longest 保留全部；元素类型不一致完全没问题；内层维度不一致 zip 不关心，但你可以在后处理里记录 len(e) 或做 padding。

## 2026-02-06

### sort函数

#### 一、sort的定位与基本特性

sort 是 **list 的原地排序方法**，调用形式为 list.sort(...)，它会直接修改原列表顺序并返回 None。它与 sorted() 的核心区别在于：sort 原地修改、仅适用于 list；sorted 返回新列表、适用于任意可迭代对象。二者底层算法相同，均为 **稳定排序 TimSort**，时间复杂度平均与最坏情况为 `O(nlog n)`，在部分有序数据上接近 O(n)。

#### **二、函数签名与参数含义**

```python
list.sort(*, key=None, reverse=False)
```

key：排序键函数，指定“按什么比较”；默认 None 表示直接比较元素本身。

reverse：是否反转排序结果；False 为升序，True 为降序。

重要性质：稳定性（相等键值的元素保持原相对顺序）、原地修改（不返回新列表）。

#### **三、比较规则与可比性约束**

当 key=None 时，元素本身必须两两可比较；当提供 key 时，比较的是 key(x) 的返回值，因此 **所有 key 返回值必须可相互比较**。Python3 不允许比较不相关类型（如 int 与 str），否则抛出 TypeError。工程修复套路：统一 key 返回类型；或返回结构化元组，在第一维放置可比较的“类型/缺失标记”。

#### **四、核心参数** key的用法与模式

key 接收一元函数，对每个元素计算一次排序键并缓存，再按键排序。

按字符串长度排序：

```py
words = ["apple", "a", "banana", "cat"]
words.sort(key=len)
```

忽略大小写排序：

```python
names = ["bob", "Alice", "carol"]
names.sort(key=str.lower)
```

按字典字段排序：

```python
rows = [{"id":3,"score":9},{"id":1,"score":2},{"id":2,"score":5}]
rows.sort(key=lambda r: r["score"])
```

按对象属性排序（更可读）：

```python
from operator import attrgetter
rows.sort(key=attrgetter("score"))
```

多关键字排序（key 返回元组，按从左到右逐字段比较）：

```python
pairs = [(1,5),(0,7),(1,2)]
pairs.sort(key=lambda x: (x[0], x[1]))
```

#### **五、**reverse **的语义与“局部降序”的实现**

整体降序：

```py
a = [3,1,2]
a.sort(reverse=True)
```

配合 key 的整体降序：

```python
pairs.sort(key=lambda x: x[1], reverse=True)
```

字段 A 升序、字段 B 降序（B 为数值）：

```python
pairs.sort(key=lambda x: (x[0], -x[1]))
```

若字段不可取负（如字符串），可用“稳定排序链式法”（见下一节）或排名映射。

#### **六、稳定排序的利用：链式多字段排序**

稳定性允许“先次要、后主要”的多次排序：

```python
rows.sort(key=lambda r: r["name"])          # 次要键
rows.sort(key=lambda r: r["score"], reverse=True)  # 主要键（降序）
```

最终效果：以 score 为主序（降序），同分时按 name 升序。

#### **七、按“数组某一维度”排序（二维/记录结构）**

二维列表按第 k 列升序/降序：

```py
rows = [[3,9],[1,2],[2,5]]
rows.sort(key=lambda r: r[0])               # 第0列升序
rows.sort(key=lambda r: r[0], reverse=True) # 第0列降序
```

多维混合方向：

```python
rows.sort(key=lambda r: (r[0], -r[1]))       # 第0列升序，第1列降序（数值）
```

字典数组按字段（含缺失处理，缺失放后）：

```python
rows.sort(key=lambda r: (r.get("score") is None, r.get("score", 0)))
```

#### **八、常见实用技巧**

排序索引而不移动原数组：

```python
a = [50,10,20]
idx = list(range(len(a)))
idx.sort(key=lambda i: a[i])
```

按绝对值排序（稳定性保留同绝对值的原顺序）：

```python
a = [-3,1,-2,5]
a.sort(key=abs)
```

自定义优先级排序（业务规则映射）：

```python
rank = {"high":0,"mid":1,"low":2}
items = ["mid","low","high","mid"]
items.sort(key=lambda x: rank.get(x, 999))
```

#### **九、常见误用与注意事项**

list.sort() 返回 None，不要写 a = a.sort()；混合不可比较类型会报错；key 返回值必须统一可比；若只需 Top-K 且数据很大，避免全量 sort（可考虑更合适的算法工具）。

#### **十、总结**

sort 的本质是“**稳定、原地、以 key 为核心的排序**”。掌握三点即可覆盖绝大多数需求：1）用 key 明确排序依据；2）用 reverse 或 key 变换控制方向；3）用稳定性实现多字段与混合方向排序。

## 2025-02-09

### 单链表查找中间节点、原地逆置

对于单链表，找二等分节点的方式是维护快慢指针，快指针的速度是慢指针的一倍

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

原地逆置，通常采用头插法，断开当前链接，插入到新链表的头部

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
```


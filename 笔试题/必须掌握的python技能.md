# lambda函数

在 Python 中，**lambda** 是一种**匿名函数**，即没有函数名的、用单条表达式构成的简洁函数。它主要用于需要一个简单函数但不想用 `def` 正式定义一个函数的场景。

---

## 1. 基本语法

```python
lambda 参数列表: 表达式
```

- **参数列表**：与普通函数的参数相同，支持位置参数、默认参数、`*args`、`**kwargs` 等。
- **表达式**：只能是一个单一的表达式，不能包含语句（如赋值 `=`、`return`、`print`、循环等）。
- **返回值**：表达式的计算结果自动作为返回值，无需 `return` 关键字。

**示例**：
```python
# 一个简单的加法 lambda
add = lambda x, y: x + y
print(add(3, 5))   # 输出 8
```

等价于普通函数：
```python
def add(x, y):
    return x + y
```

------

### 1.1 如何构造 Lambda：三步法

如果你看不懂或者不会写 `lambda`，记住这个万能公式：

$$key = \lambda \text{ 待排序列表里的元素} : \text{ 决定它顺序的那个值}$$

- **场景 1：按字符串长度排**

  `words = ["apple", "bat", "cherry"]`

  `sorted(words, key=lambda x: len(x))`  $\rightarrow$ 这里的 `x` 是单词，`len(x)` 是长度（权重）。

- **场景 2：给字典排序**

  `students = [{"name": "A", "score": 90}, {"name": "B", "score": 80}]`

  `sorted(students, key=lambda s: s["score"])` $\rightarrow$ 这里的 `s` 是字典，`s["score"]` 是分数（权重）。

- **场景 3：你的 KMeans 场景**

  `sorted(range(N), key=lambda i: init_dis[i])` $\rightarrow$ 这里的 `i` 是索引，`init_dis[i]` 是距离（权重）。

---

## 2. 为什么需要 lambda？

- **简洁**：在只需简单逻辑的地方，可以避免编写完整的函数定义。
- **临时使用**：作为高阶函数的参数（如 `sorted`、`map`、`filter`）时，一次性使用，无需命名。
- **代码紧凑**：适合函数式编程风格。

---

## 3. 常见使用场景

### 3.1 与 `sorted()` 配合，自定义排序键

```python
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
# 按年龄排序
sorted_by_age = sorted(students, key=lambda x: x[1])
print(sorted_by_age)  # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
```

### 3.2 与 `map()` 配合，批量转换

```python
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # [1, 4, 9, 16]
```

### 3.3 与 `filter()` 配合，筛选元素

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]
```

### 3.4 与 `reduce()` 配合（需从 `functools` 导入）

```python
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24
```

### 3.5 在 GUI 编程中作为临时回调

```python
import tkinter as tk
root = tk.Tk()
btn = tk.Button(root, text="Click", command=lambda: print("Clicked"))
btn.pack()
root.mainloop()
```

---

## 4. lambda 的限制

| 限制               | 说明                                                       | 示例                                                         |
| ------------------ | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **只能包含表达式** | 不能包含 `if-else`（但可以用条件表达式）、赋值、循环等语句 | `lambda x: x if x>0 else 0` 是合法的（条件表达式），但 `lambda x: if x>0: return x` 非法 |
| **不能有类型注解** | 参数和返回值不能添加类型注解                               | 普通函数可以 `def f(x: int) -> int:`                         |
| **没有文档字符串** | 无法添加 `__doc__`                                         | 调试时不够友好                                               |
| **调试困难**       | 错误堆栈中只显示 `<lambda>`，不易定位                      | 复杂逻辑建议用 `def`                                         |
| **性能无差异**     | 与普通函数性能基本相同，但创建开销略小（不存储名称）       | 微观优化意义不大                                             |

---

## 5. lambda 与普通函数的对比

| 特性             | lambda                     | 普通函数 `def`           |
| ---------------- | -------------------------- | ------------------------ |
| **名称**         | 匿名                       | 有名称                   |
| **表达式数量**   | 只能一个表达式             | 多条语句                 |
| **可读性**       | 简单逻辑清晰，复杂逻辑较差 | 适合任何复杂度的逻辑     |
| **作用域**       | 与普通函数相同（闭包）     | 相同                     |
| **返回值**       | 自动返回表达式结果         | 需显式 `return`          |
| **是否可序列化** | 不能（`pickle` 会报错）    | 可以（若在模块顶层定义） |

---

## 6. 高级技巧与注意事项

### 6.1 捕获变量（闭包）

lambda 可以捕获定义时的外部变量：

```python
def make_multiplier(n):
    return lambda x: x * n

times2 = make_multiplier(2)
print(times2(5))  # 10
```

**注意**：延迟绑定问题——当在循环中创建 lambda 并引用循环变量时，所有 lambda 会共享该变量的最终值。

```python
funcs = [lambda x: x + i for i in range(3)]
print(funcs[0](1), funcs[1](1), funcs[2](1))  # 输出 3 3 3，而非 1 2 3
```

**解决方法**：使用默认参数绑定当前值

```python
funcs = [lambda x, i=i: x + i for i in range(3)]
print(funcs[0](1), funcs[1](1), funcs[2](1))  # 2 3 4
```

### 6.2 立即调用（IIFE）

可以定义后立即调用，但实际很少这样用：

```python
result = (lambda x, y: x + y)(3, 5)
print(result)  # 8
```

### 6.3 在类属性中定义简单方法

```python
class Math:
    square = lambda self, x: x ** 2
```

不过可读性较差，不推荐。

### 6.4 与运算符模块的对比

有时 `operator` 模块中的函数比 lambda 更清晰：

```python
from operator import itemgetter, attrgetter

# 用 lambda
sorted(students, key=lambda x: x[1])

# 用 itemgetter
sorted(students, key=itemgetter(1))
```

---

## 7. 最佳实践

- **简单逻辑**（如单次使用、简单映射）→ 用 lambda。
- **复杂逻辑**（多行、包含循环/分支）→ 用 `def`。
- **需要文档或类型注解** → 用 `def`。
- **需要序列化（pickle）** → 用 `def`（模块级）。
- **在列表推导或生成器表达式中**，往往可以直接使用表达式，无需 lambda。

---

## 8. 总结

| 维度         | 说明                                              |
| ------------ | ------------------------------------------------- |
| **本质**     | 匿名函数，表达式形式                              |
| **优点**     | 简洁、临时使用、适合函数式编程                    |
| **缺点**     | 只能单表达式、可读性差、调试不便                  |
| **典型用途** | `sorted`/`map`/`filter`/`reduce` 等高阶函数的参数 |
| **替代方案** | 普通函数、`operator` 模块函数、列表推导           |

lambda 是 Python 中一个轻量级工具，合理使用可以让代码更简洁，但滥用会损害可读性。记住：**当 lambda 的逻辑变得复杂时，就该改用 `def` 了**。
"""
先实现输入一行层序遍历的数据，构建一颗二叉树；以及输入头节点，层序遍历打印这棵二叉树的节点值
"""
from collections import deque
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(data_str: str):
    """
    输入格式示例：“[1,2,3,null,null,4,5]”
    """
    if not data_str or data_str == "null":
        return None
    nodes = data_str.replace('[', '').replace(']', '').split(',')
    nodes = [n.strip() for n in nodes]
    root = TreeNode(int(nodes[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        cur = queue.popleft()
        # 处理左节点
        if i<len(nodes) and nodes[i] != "null":
            cur.left = TreeNode(int(nodes[i]))
            queue.append(cur.left)
        i+=1
        # 处理右节点
        if i<len(nodes) and nodes[i] != "null":
            cur.right = TreeNode(int(nodes[i]))
            queue.append(cur.right)
        i += 1
    return root

def print_tree(root: TreeNode):
    if not root:
        print("[]")
        return
    result = []
    q = deque([root])
    while q:
        layer = len(q)
        for _ in range(layer):
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
    while result and result[-1] == "null":
        result.pop()
    print("[" + ",".join(result) + "]")

"""
把这个输入转为二维矩阵[[1,2,3],[4,5,6],[7,8,9]]
1.json解析
2.ast解析
3.手动识别
"""
import json
input_str = "[[1,2,3],[4,5,6],[7,8,9]]"
matrix = json.loads(input_str)
print(matrix)
print(type(matrix))  # <class 'list'>
print(matrix[0][1])  # 输出 2

import ast
input_str = "[[1,2,3],[4,5,6],[7,8,9]]"
matrix = ast.literal_eval(input_str)
print(matrix)

data = input()
grid = []
tmp = []
for i in range(len(data)):
    if data[i] == "]":
        if len(tmp):
            grid.append(tmp)
        tmp = []
    elif data[i] in [",", "["]:
        continue
    else:
        tmp.append(int(data[i]))


"""
辗转相除法计算最大公约数
也可以直接math.gcd(a, b)
"""
def gcd(a:int, b:int):
    while b:
        a, b = b, a%b
    return a
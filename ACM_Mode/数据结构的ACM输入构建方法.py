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
            node = q.pop()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
    while result and result[-1] == "null":
        result.pop()
    print("[" + ",".join(result) + "]")
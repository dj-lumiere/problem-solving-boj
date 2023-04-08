# 5639 이진 검색 트리

from sys import setrecursionlimit, stdin
setrecursionlimit(200000)


class tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self, level=0):
        indent = " " * (level + 1) * 4
        left_repr = (
            f"left{level+1}={self.left.__str__(level + 1) if self.left else 'None'}"
            if self.left
            else f"left{level+1}=None"
        )
        right_repr = (
            f"right{level+1}={self.right.__str__(level + 1) if self.right else 'None'}"
            if self.right
            else f"right{level+1}=None"
        )
        if level == 0:
            return f"root={self.value}\n{indent}{left_repr}\n{indent}{right_repr}"
        else:
            return f"{self.value}\n{indent}{left_repr}\n{indent}{right_repr}"


def insert(root, value):
    if not root:
        return tree_node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value)


root = None
while True:
    try:
        value = int(stdin.readline().strip())
        root = insert(root, value)
    except:
        break
postorder_traversal(root)

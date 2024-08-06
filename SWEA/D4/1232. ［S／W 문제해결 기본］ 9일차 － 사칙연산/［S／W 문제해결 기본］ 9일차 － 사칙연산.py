class TreeNode:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def postorder(self):
        return (self.left.postorder() if self.left is not None else []) + (
            self.right.postorder() if self.right is not None else []) + [self.root]


answers = []
INF = 10 ** 18
MOD = 1_000_000_000
t = 10
for hh in range(t):
    n = int(input())
    node = ["" for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(n):
        x, y, *nodes = input().split()
        node[int(x)] = y
        for i in nodes:
            graph[int(x)].append(int(i))
    my_tree = TreeNode(node[1])
    stack = [(1, my_tree)]
    while stack:
        current_node, current_tree = stack.pop()
        if len(graph[current_node]) == 2:
            left, right = graph[current_node]
            current_tree.left = TreeNode(node[left])
            stack.append((left, current_tree.left))
            current_tree.right = TreeNode(node[right])
            stack.append((right, current_tree.right))
        if len(graph[current_node]) == 1:
            left = graph[current_node][0]
            current_tree.left = TreeNode(node[left])
            stack.append((left, current_tree.left))
    stack = []
    for i, v in enumerate(my_tree.postorder()):
        if v in "+-*/":
            b, a = stack.pop(), stack.pop()
            result = 0.0
            if v == "+":
                result = a + b
            elif v == "-":
                result = a - b
            elif v == "*":
                result = a * b
            else:
                result = a / b
            stack.append(result)
        else:
            stack.append(float(v))
    answer = int(stack[0])
    answers.append(f"#{hh + 1} {answer}")
print(*answers, sep="\n")

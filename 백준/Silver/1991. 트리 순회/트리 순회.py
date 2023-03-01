# 1991 트리 순회

N = int(input())
tree = dict()
for i in range(N):
    root, left, right = list(map(str, input().split(" ")))
    tree[root] = (left, right)


def preorder(root: str) -> list[str]:
    if tree[root][0] == ".":
        left = []
    else:
        left = preorder(tree[root][0])
    if tree[root][1] == ".":
        right = []
    else:
        right = preorder(tree[root][1])
    return [root] + left + right


def inorder(root: str) -> list[str]:
    if tree[root][0] == ".":
        left = []
    else:
        left = inorder(tree[root][0])
    if tree[root][1] == ".":
        right = []
    else:
        right = inorder(tree[root][1])
    return left + [root] + right


def postorder(root: str) -> list[str]:
    if tree[root][0] == ".":
        left = []
    else:
        left = postorder(tree[root][0])
    if tree[root][1] == ".":
        right = []
    else:
        right = postorder(tree[root][1])
    return left + right + [root]


print(*preorder("A"), sep="")
print(*inorder("A"), sep="")
print(*postorder("A"), sep="")
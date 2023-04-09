# 15900 나무 탈출

from sys import stdin, setrecursionlimit
setrecursionlimit(500000)


N = int(stdin.readline().strip())
parent_child_dict = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    a, b = map(int, stdin.readline().strip().split())
    parent_child_dict[a].append(b)
    parent_child_dict[b].append(a)
visited = [False for i in range(N + 1)]
distance = [0 for i in range(N + 1)]
is_leaf_list = [True for i in range(N + 1)]


def traverse_tree(node: int, tree: dict[int, list[int]]) -> None:
    visited[node] = True
    is_leaf = True
    for child in tree[node]:
        if not visited[child]:
            distance[child] = distance[node] + 1
            traverse_tree(child, tree)
            is_leaf = False
    if not is_leaf:
        is_leaf_list[node] = False


traverse_tree(1, parent_child_dict)
answer = sum([j for (i, j) in zip(is_leaf_list, distance) if i])
if answer % 2:
    print("Yes")
else:
    print("No")

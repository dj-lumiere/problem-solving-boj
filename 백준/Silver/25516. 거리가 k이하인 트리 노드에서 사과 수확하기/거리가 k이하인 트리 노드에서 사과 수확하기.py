# 25516 거리가 k이하인 트리 노드에서 사과 수확하기

from sys import stdin, setrecursionlimit
setrecursionlimit(200000)

n, k = map(int, stdin.readline().strip().split(" "))
parent_child_dict: dict[int, list[int]] = {i: [] for i in range(n)}
for i in range(n - 1):
    a, b = map(int, stdin.readline().strip().split(" "))
    parent_child_dict[a].append(b)
    parent_child_dict[b].append(a)
apple_count: list[int] = list(map(int, stdin.readline().strip().split(" ")))
visited: list[bool] = [False for i in range(n)]
distance: list[int] = [0 for i in range(n)]


def traverse_tree(node: int, tree: dict[int, list[int]]) -> None:
    visited[node] = True
    for child in tree[node]:
        if not visited[child]:
            distance[child] = distance[node] + 1
            traverse_tree(child, tree)


traverse_tree(0, parent_child_dict)

print(sum([i for (i, j) in zip(apple_count, distance) if j <= k]))

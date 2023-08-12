# 11437 LCA
from itertools import zip_longest
from sys import stdin, stdout
input = stdin.readline
print = stdout.write


def construct_path(depth: list[int], parent: list[int], node: int) -> list[int]:
    current_node = node
    next_node = parent[current_node]
    path = []
    for _ in range(depth[node] + 1):
        path.append(current_node)
        current_node, next_node = next_node, parent[next_node]
    path.reverse()
    return path


def find_lca(depth: list[int], parent: list[int], a: int, b: int) -> int:
    result = 0
    path_a = construct_path(depth, parent, a)
    path_b = construct_path(depth, parent, b)
    for i, j in zip_longest(path_a, path_b, fillvalue=0):
        if i != j:
            break
        result = i
    return result


def dfs(adjacent_node: list[list[int]], depth: list[int], parent: list[int], N: int):
    dfs_stack = [(1, 0, 0)]
    visited = [False] * (N + 1)
    while dfs_stack:
        current_node, current_depth, current_parent = dfs_stack.pop()
        depth[current_node] = current_depth
        parent[current_node] = current_parent
        visited[current_node] = True
        for next_node in adjacent_node[current_node]:
            if visited[next_node]:
                continue
            if depth[next_node] != 0 and parent[next_node] != 0:
                continue
            if next_node == current_node:
                continue
            dfs_stack.append((next_node, current_depth + 1, current_node))


N = int(input())
adjacent_node: list[list[int]] = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split(" "))
    adjacent_node[a].append(b)
    adjacent_node[b].append(a)
depth = [0] * (N + 1)
parent = [0] * (N + 1)
dfs(adjacent_node, depth, parent, N)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split(" "))
    print(f"{find_lca(depth, parent, a, b)}\n")
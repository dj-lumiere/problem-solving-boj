# 11438 LCA 2
from itertools import zip_longest
from sys import stdin, stdout
from math import ceil, log2

input = stdin.readline
print = stdout.write
MAX_STEP = ceil(log2(10**5))


def find_lca(
    a: int, b: int, depth: list[int], ancestor_power_of_2: list[list[int]]
) -> int:
    if depth[a] > depth[b]:
        a, b = b, a
    for i in range(MAX_STEP - 1, -1, -1):
        if depth[b] - depth[a] >= 2**i:
            b = ancestor_power_of_2[b][i]
    if a == b:
        return a
    for i in range(MAX_STEP - 1, -1, -1):
        if ancestor_power_of_2[a][i] != ancestor_power_of_2[b][i]:
            a = ancestor_power_of_2[a][i]
            b = ancestor_power_of_2[b][i]
    return ancestor_power_of_2[a][0]


def dfs(adjacent_node: list[list[int]], N: int) -> tuple[list[int], list[list[int]]]:
    NOT_FOUND = -1
    dfs_stack: list[tuple[int, int]] = [(1, NOT_FOUND)]
    depth = [0] * (N + 1)
    ancestor_power_of_2 = [[NOT_FOUND] * MAX_STEP for _ in range(N + 1)]
    while dfs_stack:
        current_node, current_parent = dfs_stack.pop()
        ancestor_power_of_2[current_node][0] = current_parent
        for power in range(1, MAX_STEP):
            if ancestor_power_of_2[current_node][power - 1] != NOT_FOUND:
                ancestor_power_of_2[current_node][power] = ancestor_power_of_2[
                    ancestor_power_of_2[current_node][power - 1]
                ][power - 1]
        for next_node in adjacent_node[current_node]:
            if next_node == current_parent:
                continue
            depth[next_node] = depth[current_node] + 1
            dfs_stack.append((next_node, current_node))
    return depth, ancestor_power_of_2


N = int(input())
adjacent_node: list[list[int]] = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split(" "))
    adjacent_node[a].append(b)
    adjacent_node[b].append(a)
depth, ancestor_power_of_2 = dfs(adjacent_node, N)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split(" "))
    print(f"{find_lca(a, b, depth, ancestor_power_of_2)}\n")
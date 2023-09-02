# 20040 사이클 게임

from sys import stdin


def input():
    return stdin.readline().strip()


def union(x, y, parent):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x != root_y:
        parent[root_x] = root_y


def find(x, parent):
    nodes = []
    while x != parent[x]:
        nodes.append(x)
        x = parent[x]
    for node in nodes:
        parent[node] = x
    return x


def is_connected(a, b, parent):
    parent_a = find(a, parent)
    parent_b = find(b, parent)
    return parent_a == parent_b


N, M = map(int, input().split(" "))
answer = 0
parent = [i for i in range(N + 1)]
for i in range(1, M + 1):
    a, b = map(int, input().split(" "))
    if is_connected(a, b, parent):
        answer = i
        break
    union(a, b, parent)
print(answer)
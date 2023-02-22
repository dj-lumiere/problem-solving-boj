# 11725 트리의 부모 찾기

from collections import deque
from sys import stdin

N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]
parent[1] = 1
for _ in range(N - 1):
    a, b = list(map(int, stdin.readline().strip().split(" ")))
    tree[a].append(b)
    tree[b].append(a)
bfs_queue: deque[tuple] = deque()
for i in tree[1]:
    bfs_queue.append((i, 1))
while bfs_queue:
    y, x = bfs_queue.popleft()
    if parent[y] == 0:
        parent[y] = x
    for i in tree[y]:
        if parent[i] == 0:
            bfs_queue.append((i, y))
print(*parent[2:], sep="\n")

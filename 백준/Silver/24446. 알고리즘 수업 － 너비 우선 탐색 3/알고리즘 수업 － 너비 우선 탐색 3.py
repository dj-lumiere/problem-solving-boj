# 24446 알고리즘 수업 - 너비 우선 탐색 3

from collections import deque
from sys import stdin, stdout

input = stdin.readline
print = stdout.write
NOT_VISITED = -1

N, M, R = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split(" "))
    graph[u].append(v)
    graph[v].append(u)
depth = [NOT_VISITED for _ in range(N + 1)]

bfs_deque = deque([(0, R)])
while bfs_deque:
    distance, current_vertex = bfs_deque.popleft()
    if depth[current_vertex] == NOT_VISITED:
        depth[current_vertex] = distance
    for next_vertex in graph[current_vertex]:
        if depth[next_vertex] == NOT_VISITED:
            bfs_deque.append((distance + 1, next_vertex))

answer = "\n".join(map(str, depth[1:]))
print(f"{answer}")

# 2623 음악프로그램

from collections import deque
from sys import stdin


def input():
    return stdin.readline().strip()


def topological_sort(n, graph):
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in graph[i]:
            indegree[j] += 1
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    return result


N, M = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    _, *singer_order = map(int, input().split(" "))
    for i, v in enumerate(singer_order):
        if i == 0:
            continue
        graph[singer_order[i - 1]].append(v)
final_order = topological_sort(N, graph)
if len(final_order) != N:
    print(0)
else:
    print(*final_order, sep="\n")
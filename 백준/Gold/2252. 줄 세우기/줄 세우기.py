# 2252 줄 세우기

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
    a, b = map(int, input().split(" "))
    graph[a].append(b)

print(*topological_sort(N, graph), sep=" ")
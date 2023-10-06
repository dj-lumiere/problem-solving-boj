# 1766 문제집

from heapq import heappush, heappop
from sys import stdin


def input():
    return stdin.readline().strip()


def topological_sort(n, graph):
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in graph[i]:
            indegree[j] += 1
    queue = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heappush(queue, i)
    result = []
    while queue:
        u = heappop(queue)
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heappush(queue, v)

    return result


N, M = map(int, input().split(" "))
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
final_order = topological_sort(N, graph)
print(*final_order)
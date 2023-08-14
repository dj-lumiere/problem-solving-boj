# 1504 특정한 최단 경로

from heapq import heappop, heappush
from sys import stdin


def graphify(graph_list: list[list[tuple[int, int]]], M: int):
    for _ in range(M):
        a, b, c = list(map(int, input().split(" ")))
        graph_list[a].append((b, c))
        graph_list[b].append((a, c))


def dijkstra(graph_list: list[list[tuple[int, int]]], init: int, dest: int):
    heap = []
    heappush(heap, (0, init))
    cost_list = [INF for _ in range(N + 1)]
    cost_list[init] = 0
    while heap:
        cost, next_node = heappop(heap)
        if cost_list[next_node] < cost:
            continue
        if next_node == dest:
            return cost_list[dest]
        for i, j in graph_list[next_node]:
            next_cost = cost + j
            if next_cost >= cost_list[i]:
                continue
            cost_list[i] = next_cost
            heappush(heap, (next_cost, i))
    return INF


def input():
    return stdin.readline().strip()


N, M = map(int, input().split(" "))
INF = 10**9
graph_list = [[] for _ in range(N + 1)]
graphify(graph_list, M)
mid1, mid2 = map(int, input().split(" "))
result1 = (
    dijkstra(graph_list, 1, mid1)
    + dijkstra(graph_list, mid1, mid2)
    + dijkstra(graph_list, mid2, N)
)
result2 = (
    dijkstra(graph_list, 1, mid2)
    + dijkstra(graph_list, mid2, mid1)
    + dijkstra(graph_list, mid1, N)
)
result = min(result1, result2)
print(-1 if result >= INF else result)
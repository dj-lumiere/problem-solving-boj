# 1753 최단경로

from heapq import heappop, heappush
from sys import stdin
from math import inf

# bfs처럼 나가는데 빠른 것들이 앞으로 계속 땡겨짐
N, M = list(map(int, input().split(" ")))
init = int(input())

graph_list = [[] for _ in range(N + 1)]


def graphify(M):
    for _ in range(M):
        a, b, c = list(map(int, stdin.readline().rstrip().split(" ")))
        graph_list[a].append((b, c))


# init = 1
# N = 5
# graph_list = [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]
graphify(M)
cost_list = [inf for _ in range(N + 1)]
cost_list[init] = 0


def dijkstra(init):
    heap = []
    heappush(heap, (0, init))
    path_final = []
    while heap:
        cost, next_node = heappop(heap)
        if cost_list[next_node] < cost:
            continue
        else:
            for i, j in graph_list[next_node]:
                next_cost = cost + j
                if next_cost < cost_list[i]:
                    cost_list[i] = next_cost
                    heappush(heap, (next_cost, i))
dijkstra(init)

for i in range(1, N + 1):
    if cost_list[i] == inf:
        print("INF")
    else:
        print(cost_list[i])
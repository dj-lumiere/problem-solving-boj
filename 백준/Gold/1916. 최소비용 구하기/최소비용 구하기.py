# 1916 최소비용 구하기

from heapq import heappop, heappush
from sys import stdin
from math import inf

# bfs처럼 나가는데 빠른 것들이 앞으로 계속 땡겨짐
N, M = int(input()), int(input())
graph_list = [[] for i in range(0, N + 1)]
road_list = [[inf for _ in range(N + 1)] for i in range(0, N + 1)]


def graphify(M):
    for _ in range(M):
        a, b, c = list(map(int, stdin.readline().rstrip().split(" ")))
        graph_list[a].append(b)
        road_list[a][b] = min(road_list[a][b], c)


graphify(M)

init, dst = list(map(int, stdin.readline().rstrip().split(" ")))


def dijkstra(init, dst) -> int:
    if init == dst:
        return 0
    else:
        heap = []
        heappush(heap, (0, init))
        cost_list = [inf for _ in range(N + 1)]
        while heap:
            cost, next_node = heappop(heap)
            if cost_list[dst] < cost:
                continue
            else:
                for i in graph_list[next_node]:
                    next_cost = cost + road_list[next_node][i]
                    if next_cost < cost_list[i]:
                        cost_list[i] = next_cost
                        heappush(heap, (next_cost, i))
        return cost_list[dst]


print(dijkstra(init, dst))

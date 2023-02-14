# 11779 최소비용 구하기 2

from heapq import heappop, heappush
from sys import stdin
from math import inf

# bfs처럼 나가는데 빠른 것들이 앞으로 계속 땡겨짐
N, M = int(input()), int(input())
graph_list = [[False for _ in range(N + 1)] for i in range(0, N + 1)]
road_list = [[inf for _ in range(N + 1)] for i in range(0, N + 1)]


def graphify(M):
    for _ in range(M):
        a, b, c = list(map(int, stdin.readline().rstrip().split(" ")))
        graph_list[a][b] = True
        road_list[a][b] = min(road_list[a][b], c)


graphify(M)

init, dst = list(map(int, stdin.readline().rstrip().split(" ")))

cost_list = [inf for _ in range(N + 1)]


def dijkstra(init, dst) -> tuple:
    if init == dst:
        return (0, [init])
    else:
        heap = []
        heappush(heap, (0, init, [init]))
        path_final = []
        while heap:
            cost, next_node, path = heappop(heap)
            if cost_list[dst] < cost:
                continue
            else:
                for i, j in zip(range(N + 1), graph_list[next_node]):
                    if j:
                        next_cost = cost + road_list[next_node][i]
                        if next_cost < cost_list[i]:
                            cost_list[i] = next_cost
                            if i == dst:
                                path_final = path[:] + [i]
                            heappush(heap, (next_cost, i, path + [i]))
        return cost_list[dst], path_final


final_cost, final_path = dijkstra(init, dst)
print(final_cost)
print(len(final_path))
print(" ".join(map(str, final_path)))

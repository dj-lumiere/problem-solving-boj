# 30985 직장인 파댕이의 사회생활

from heapq import heappop, heappush


INF = 10**18


def dijkstra(init, dst, graph, elevator, floor):
    if init == dst:
        return 0
    heap = []
    heappush(heap, (0, 0, init))
    if elevator[init] != INF:
        heappush(heap, (1, elevator[init] * (floor - 1), init))
    cost_list = [[INF for _ in range(len(graph))] for _ in range(2)]
    while heap:
        elevator_used, cost, next_node = heappop(heap)
        if next_node == dst and elevator_used:
            return cost
        for i in graph[next_node]:
            dest, cost_sub = i
            next_cost = cost + cost_sub
            if next_cost < cost_list[elevator_used][dest]:
                cost_list[elevator_used][dest] = next_cost
                heappush(heap, (elevator_used, next_cost, dest))
            if not elevator_used:
                if next_cost + elevator[next_node] * (floor - 1) < cost_list[1][dest]:
                    cost_list[1][dest] = next_cost + elevator[next_node] * (floor - 1)
                    heappush(
                        heap, (1, next_cost + elevator[next_node] * (floor - 1), dest)
                    )
    return INF


N, M, K = map(int, input().split(" "))

hallway = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, cost = map(int, input().split(" "))
    hallway[start].append((end, cost))
    hallway[end].append((start, cost))

for i in range(1, N + 1):
    hallway[i].append((i, 0))

elevator = [INF] + list(map(int, input().split(" ")))
for i, v in enumerate(elevator):
    if v == -1:
        elevator[i] = INF

total_cost = dijkstra(1, N, hallway, elevator, K)
print(-1 if total_cost >= INF else total_cost)

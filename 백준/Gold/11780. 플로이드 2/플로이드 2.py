# 11780 플로이드 2
from itertools import product

N, M = int(input()), int(input())
INF = 10**9
distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
original_waypoint = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
waypoint = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split(" "))
    distance[start][end] = min(cost, distance[start][end])
    original_waypoint[start][end] = 1
    waypoint[start][end] = end
for mid, start, end in product(range(1, N + 1), range(1, N + 1), range(1, N + 1)):
    if start == end:
        distance[start][end] = 0
        continue
    if distance[start][mid] + distance[mid][end] < distance[start][end]:
        distance[start][end] = distance[start][mid] + distance[mid][end]
        waypoint[start][end] = waypoint[start][mid]
for i in range(1, N + 1):
    new_list = []
    for j in range(1, N + 1):
        if distance[i][j] == INF:
            new_list.append("0")
            continue
        new_list.append(str(distance[i][j]))
    print(" ".join(new_list))
for i, j in product(range(1, N + 1), range(1, N + 1)):
    if i == j or distance[i][j] == INF:
        print(0)
        continue
    path = []
    next_node = i
    while next_node != j:
        path.append(next_node)
        next_node = waypoint[next_node][j]
    path.append(j)
    print(len(path), *path, sep=" ")
    path.clear()

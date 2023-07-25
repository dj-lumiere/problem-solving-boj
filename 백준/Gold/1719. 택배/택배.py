# 1719 택배
from itertools import product

N, M = map(int, input().split(" "))
INF = 10**9
distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
original_waypoint = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
waypoint = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split(" "))
    distance[start][end] = cost
    distance[end][start] = cost
    original_waypoint[end][start] = 1
    original_waypoint[start][end] = 1
    waypoint[end][start] = start
    waypoint[start][end] = end
for mid, start, end in product(range(1, N + 1), range(1, N + 1), range(1, N + 1)):
    if start == end:
        distance[start][end] = 0
        continue
    if distance[start][end] > distance[start][mid] + distance[mid][end]:
        distance[start][end] = distance[start][mid] + distance[mid][end]
        waypoint[start][end] = waypoint[start][mid]
for i in range(1, N + 1):
    new_list = []
    for j in range(1, N + 1):
        if i != j:
            new_list.append(str(waypoint[i][j]))
        else:
            new_list.append("-")
    print(" ".join(new_list))

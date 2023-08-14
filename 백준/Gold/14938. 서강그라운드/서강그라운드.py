# 14938 서강그라운드

from itertools import product
from sys import stdin

input = stdin.readline
N, M, R = map(int, input().split(" "))
item_count = [0] + list(map(int, input().split(" ")))
INF = 10**9
distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
max_item_count_from_node = [0] * (N + 1)
for _ in range(R):
    start, end, cost = map(int, input().split(" "))
    distance[start][end] = min(cost, distance[start][end])
    distance[end][start] = min(cost, distance[end][start])
for mid, start, end in product(range(1, N + 1), range(1, N + 1), range(1, N + 1)):
    if start == end:
        distance[start][end] = 0
        continue
    if distance[start][mid] + distance[mid][end] < distance[start][end]:
        distance[start][end] = distance[start][mid] + distance[mid][end]
for i in range(1, N + 1):
    max_item_count_from_node[i] = sum(
        item_count[j] * (distance[i][j] <= M) for j in range(1, N + 1)
    )
print(max(max_item_count_from_node))
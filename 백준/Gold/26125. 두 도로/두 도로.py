# 26125 두 도로
# AB CD -> S->T, S->A->B->T, S->C->D->T, S->A->B->C->D->T, S->C->D->A->B->T

from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


INF = 10**12


def query(road1_start, road1_end, cost1, road2_start, road2_end, cost2):
    return min(
        distance[S][T],
        distance[S][road1_start] + cost1 + distance[road1_end][T],
        distance[S][road2_start] + cost2 + distance[road2_end][T],
        distance[S][road1_start]
        + cost1
        + distance[road1_end][road2_start]
        + cost2
        + distance[road2_end][T],
        distance[S][road2_start]
        + cost2
        + distance[road2_end][road1_start]
        + cost1
        + distance[road1_end][T],
        INF,
    )
    pass


N, M, S, T = map(int, input().split(" "))
distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    distance[i][i] = 0
for _ in range(M):
    start, end, cost = map(int, input().split(" "))
    distance[start][end] = min(distance[start][end], cost)
for mid, start, end in product(range(1, N + 1), repeat=3):
    distance[start][end] = min(
        distance[start][end], distance[start][mid] + distance[mid][end], INF
    )
Q = int(input())
for _ in range(Q):
    road1_start, road1_end, cost1, road2_start, road2_end, cost2 = map(
        int, input().split(" ")
    )
    result = query(road1_start, road1_end, cost1, road2_start, road2_end, cost2)
    if result == INF:
        print(-1)
    else:
        print(result)
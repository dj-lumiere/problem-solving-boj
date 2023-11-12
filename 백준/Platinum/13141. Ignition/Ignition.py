# 13141 Ignition
from itertools import product
from sys import stdin


def input():
    return stdin.readline().strip()


INF = 10**18
N, M = map(int, input().split(" "))
minimal_length = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
maximal_length = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    minimal_length[i][i] = 0
for _ in range(M):
    S, E, L = map(int, input().split(" "))
    minimal_length[S][E] = min(minimal_length[S][E], L)
    minimal_length[E][S] = min(minimal_length[E][S], L)
    maximal_length[S][E] = max(maximal_length[S][E], L)
    maximal_length[E][S] = max(maximal_length[E][S], L)
for m, s, e in product(range(1, N + 1), repeat=3):
    minimal_length[s][e] = min(
        minimal_length[s][e], minimal_length[s][m] + minimal_length[m][e]
    )

answer = INF
for s in range(1, N + 1):
    temp = 0
    for e in range(1, N + 1):
        for m in range(e, N + 1):
            if maximal_length[e][m] == 0:
                continue
            temp = max(
                temp, minimal_length[s][e] + minimal_length[s][m] + maximal_length[e][m]
            )
    answer = min(answer, temp)
print(f"{answer / 2:.1f}")
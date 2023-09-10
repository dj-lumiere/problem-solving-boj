# H번 - 줄줄이 박수
from sys import stdin


def input():
    return stdin.readline().strip()


N, M = map(int, input().split(" "))
grid = [0 for _ in range(M)]
for _ in range(N):
    grid_sub = list(map(int, input().split(" ")))
    for i in range(M):
        grid[i] += grid_sub[i]
grid_accsum = [0]
for _, v in enumerate(grid):
    grid_accsum.append(grid_accsum[-1] + v)
A = int(input())
max_clap = 0
for i in range(M + 1):
    if i < A:
        continue
    max_clap = max(max_clap, grid_accsum[i] - grid_accsum[i - A])
print(max_clap)
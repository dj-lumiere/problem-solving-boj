# 30032 알파벳 뒤집기

from itertools import product

upside_down = {"d": "q", "b": "p", "q": "d", "p": "b"}
leftside_right = {"d": "b", "b": "d", "q": "p", "p": "q"}

N, D = map(int, input().split(" "))
grid = [list(input()) for _ in range(N)]
for i, j in product(range(N), repeat=2):
    if D == 1:
        grid[i][j] = upside_down[grid[i][j]]
    elif D == 2:
        grid[i][j] = leftside_right[grid[i][j]]
for i in range(N):
    print(*grid[i], sep="")
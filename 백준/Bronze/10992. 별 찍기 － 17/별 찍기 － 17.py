# 10992 별 찍기 - 17
N = int(input())
# 그리드 하나 만들기
grid = [[" " for _ in range(2 * N - 1)] for _ in range(N)]
for i in range(N):
    grid[i][N - 1 - i] = "*"
    grid[i][N - 1 + i] = "*"
grid[-1] = ["*"] * (2 * N - 1)
for i in range(N - 1):
    for j in range(N + i, 2 * N - 1):
        grid[i][j] = ""
print(*["".join(i) for i in grid], sep="\n")
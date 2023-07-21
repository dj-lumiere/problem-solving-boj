# 1149 RGB거리

INVALID = 10**9
N = int(input())
color = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(N)]
for j in range(3):
    dp[0][j] = color[0][j]
for i in range(N):
    if i == 0:
        continue
    for j in range(3):
        dp[i][j] = (
            min([dp[i - 1][k] if k != j else INVALID for k in range(3)]) + color[i][j]
        )
print(min(dp[-1][j] for j in range(3)))

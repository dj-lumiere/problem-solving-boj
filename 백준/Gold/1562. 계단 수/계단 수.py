# 1562 계단 수
from itertools import product

MOD = 1000000000
N = int(input())
dp = [[[0] * 1024 for _ in range(10)] for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i][1 << i] = 1
for i, j, k in product(range(2, N + 1), range(10), range(1024)):
    if j == 0:
        dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k]
        dp[i][j][k | (1 << j)] %= MOD
        continue
    if j == 9:
        dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k]
        dp[i][j][k | (1 << j)] %= MOD
        continue
    dp[i][j][k | (1 << j)] += dp[i - 1][j - 1][k]
    dp[i][j][k | (1 << j)] += dp[i - 1][j + 1][k]
    dp[i][j][k | (1 << j)] %= MOD
result = 0
for j in range(10):
    result += dp[N][j][1023]
    result %= MOD
print(result)
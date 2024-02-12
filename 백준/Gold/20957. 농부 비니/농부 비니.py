# 20957 농부 비니

from itertools import product

MOD = 10**9 + 7
dp = [[[0 for _ in range(7)] for _ in range(7)] for _ in range(10000)]
for i in range(10000):
    for j in range(10):
        if i == 0 and j == 0:
            continue
        if i == 0:
            dp[0][j % 7][j % 7] += 1
            continue
        for a, b in product(range(7), repeat=2):
            dp[i][(a + j) % 7][(b * j) % 7] += dp[i - 1][a][b]
            dp[i][(a + j) % 7][(b * j) % 7] %= MOD
T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N - 1][0][0])
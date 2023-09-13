# 16565 N포커

from itertools import product

MOD = 10007

combinations = [[0] * 53 for i in range(52 + 1)]
for i, j in product(range(53), repeat=2):
    if j == 0 or j == i:
        combinations[i][j] = 1
        continue
    if j > i:
        continue
    combinations[i][j] = combinations[i - 1][j] + combinations[i - 1][j - 1] % MOD

N = int(input())
result = 0
for i in range(N // 4 + 1):
    if i == 0:
        continue
    if i & 1:
        result += combinations[13][i] * combinations[52 - 4 * i][N - 4 * i]
        result %= MOD
    else:
        result -= combinations[13][i] * combinations[52 - 4 * i][N - 4 * i]
        result %= MOD
print(result)
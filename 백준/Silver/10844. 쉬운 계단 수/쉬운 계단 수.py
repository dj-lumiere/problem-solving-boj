# 10844 쉬운 계단 수
from itertools import product

MOD = 1_000_000_000
N = int(input())
stair_number = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N)]
stair_number[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i, j in product(range(N), range(10)):
    if i == 0:
        continue
    if j == 0:
        stair_number[i][j] = stair_number[i - 1][j + 1] % MOD
        continue
    if j == 9:
        stair_number[i][j] = stair_number[i - 1][j - 1] % MOD
        continue
    stair_number[i][j] = (stair_number[i - 1][j - 1] + stair_number[i - 1][j + 1]) % MOD
print(sum(stair_number[-1]) % MOD)
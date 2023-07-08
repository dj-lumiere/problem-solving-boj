# 28294 프랙탈

# N**a*(1/(1-(N-2)/N))*N

MOD = 10**9 + 7
N, a = map(int, input().split(" "))
print((pow(N, a + 1, MOD) + N * (N - 2) * (pow(N, a, MOD) - pow(N - 1, a, MOD))) % MOD)
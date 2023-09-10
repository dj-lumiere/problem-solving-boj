# 29719 브실이의 불침번 근무
# M**N-(M-1)**N

from sys import stdin


def input():
    return stdin.readline().strip()


MOD = 1_000_000_007
N, M = map(int, input().split(" "))
print((pow(M, N, MOD) - pow(M - 1, N, MOD)) % MOD)

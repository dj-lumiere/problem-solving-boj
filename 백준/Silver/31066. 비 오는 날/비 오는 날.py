# 31066 비 오는 날


def sol(N, M, K):
    if N != 1 and M * K == 1:
        return -1
    if N == 1 and M * K == 1:
        return 1
    return 1 + ((max(0, N - M * K) + M * K - 2) // (M * K - 1)) * 2


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    print(sol(N, M, K))
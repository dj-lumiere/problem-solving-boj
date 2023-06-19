# 2444 별 찍기 - 7
N = int(input())
for i in range(N - 1, -1, -1):
    print(" " * i + "*" * (2 * N - 1 - 2 * i))
for i in range(1, N):
    print(" " * i + "*" * (2 * N - 1 - 2 * i))
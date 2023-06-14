# 2443 별 찍기 - 6

N = int(input())
for i in range(N):
    print(" " * i + "*" * (2 * N - 1 - 2 * i))
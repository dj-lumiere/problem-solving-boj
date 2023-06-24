# 2446 별 찍기 - 9
N = int(input())

for i in range(0, N - 1):
    print(" " * i + "*" * (2 * N - 1 - 2 * i))
for i in range(N - 1, -1, -1):
    print(" " * i + "*" * (2 * N - 1 - 2 * i))
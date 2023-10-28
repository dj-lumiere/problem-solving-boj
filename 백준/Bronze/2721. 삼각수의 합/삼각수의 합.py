# 2721 삼각수의 합
triangle = lambda n: n * (n + 1) // 2
T = int(input())
for _ in range(T):
    N = int(input())
    print(sum(triangle(i + 1) * i for i in range(1, N + 1)))
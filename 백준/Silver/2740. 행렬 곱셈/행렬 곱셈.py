# 2740 행렬 곱셈

N, M = list(map(int, input().split(" ")))
A = [list(map(int, input().split(" "))) for _ in range(N)]
M, K = list(map(int, input().split(" ")))
B = [list(map(int, input().split(" "))) for _ in range(M)]
result = [
    [sum([A[j][k] * B[k][i] for k in range(M)]) for i in range(K)] for j in range(N)
]
for j in range(N):
    print(*result[j])
# 1551 수열의 변화

N, K = map(int, input().split())
A = list(map(int, input().split(",")))
for _ in range(K):
    result = []
    for i, v in enumerate(A):
        if i == 0:
            continue
        result.append(v - A[i - 1])
    A = result
print(*A, sep=",")
# 11055 가장 긴 증가하는 부분 수열 4

N = int(input())
A = list(map(int, input().split(" ")))

dp_len = [1] * N
dp_path = [[j] for i, j in enumerate(A)]
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            if dp_len[i] < dp_len[j] + 1:
                dp_path[i] = dp_path[j][:] + [A[i]]
                dp_len[i] = dp_len[j] + 1
print(max(dp_len))
print(" ".join(map(str, dp_path[dp_len.index(max(dp_len))])))
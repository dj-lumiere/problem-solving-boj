# 11053 가장 긴 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split(" ")))
lis_length = [1 for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            lis_length[i] = max(lis_length[i], lis_length[j] + 1)
print(max(lis_length))
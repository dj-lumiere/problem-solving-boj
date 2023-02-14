# 2565 전깃줄

N = int(input())
A = [0 for i in range(500 + 1)]
for _ in range(N):
    a_sub, b_sub = list(map(int, input().split(" ")))
    A[b_sub] = a_sub
A = [j for i, j in enumerate(A) if j != 0]
dp = [1] * (N)
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and A[j] != 0:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))
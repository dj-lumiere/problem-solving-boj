# 2143 두 배열의 합

from collections import defaultdict

T: int = int(input())
n: int = int(input())
A: list[int] = list(map(int, input().split(" ")))
m: int = int(input())
B: list[int] = list(map(int, input().split(" ")))
answer: int = 0
A_accumulated_sum: list[int] = [0]
B_accumulated_sum: list[int] = [0]
for i in range(n):
    A_accumulated_sum.append(A_accumulated_sum[-1] + A[i])
for i in range(m):
    B_accumulated_sum.append(B_accumulated_sum[-1] + B[i])
A_dp: dict[int, int] = defaultdict()
B_dp: dict[int, int] = defaultdict()
for i in range(1, n + 1):
    for j in range(0, i):
        sub_value = A_accumulated_sum[i] - A_accumulated_sum[j]
        if sub_value not in A_dp:
            A_dp[sub_value] = 1
        else:
            A_dp[sub_value] += 1
for i in range(1, m + 1):
    for j in range(0, i):
        sub_value = B_accumulated_sum[i] - B_accumulated_sum[j]
        if sub_value not in B_dp:
            B_dp[sub_value] = 1
        else:
            B_dp[sub_value] += 1
for a_sum, a_count in A_dp.items():
    if T - a_sum in B_dp:
        answer += a_count * B_dp[T - a_sum]
print(answer)
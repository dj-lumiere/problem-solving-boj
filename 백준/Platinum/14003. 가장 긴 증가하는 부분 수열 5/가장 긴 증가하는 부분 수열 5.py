# 14003 가장 긴 증가하는 부분 수열 5
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split(" ")))

dp_tail = [0] * N
dp_prev = [-1] * N
j_list = []
lis_len = 0
for i in range(N):
    if not j_list or j_list[-1] < A[i]:
        j = lis_len
        j_list.append(A[i])
    else:
        j = bisect_left(j_list, A[i])
    if j == lis_len:
        dp_tail[lis_len] = i
        j_list[lis_len] = A[i]
        dp_prev[i] = dp_tail[lis_len - 1] if lis_len > 0 else -1
        lis_len += 1
    elif A[i] < A[dp_tail[j]]:
        dp_tail[j] = i
        j_list[j] = A[i]
        dp_prev[i] = dp_tail[j - 1] if j > 0 else -1
lis = []
p = dp_tail[lis_len-1]
while p != -1:
    lis.append(A[p])
    p = dp_prev[p]
lis = lis[::-1]

print(lis_len)
print(*lis, sep=" ")
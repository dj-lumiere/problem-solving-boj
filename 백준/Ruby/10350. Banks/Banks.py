# 10350 Banks
from math import ceil
from sys import stdin, stdout

input = stdin.readline
print = stdout.write
N = int(input().strip())
k = list(map(int, input().strip().split(" ")))
k_acc_sum = [0]
for value in k:
    k_acc_sum.append(k_acc_sum[-1] + value)
for value in k:
    k_acc_sum.append(k_acc_sum[-1] + value)
total_sum = k_acc_sum[-1] // 2
answer = 0
for offset in range(N):
    for items in range(N):
        index_end = items + offset + 1
        index_start = offset
        acc_sum = k_acc_sum[index_end] - k_acc_sum[index_start]
        if acc_sum < 0:
            answer += ceil(-acc_sum / total_sum)
print(f"{answer}")
# 25916 싫은데요
from sys import stdin, stdout
from bisect import bisect_left

input = stdin.readline
print = stdout.write

N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
A_accumulated_sum = [0]
for value in A:
    A_accumulated_sum.append(A_accumulated_sum[-1] + value)
answer = 0
for index, value in enumerate(A_accumulated_sum):
    target = bisect_left(A_accumulated_sum, value + M)
    if target == len(A_accumulated_sum):
        answer = max(answer, A_accumulated_sum[-1] - value)
    elif A_accumulated_sum[target] - value <= M:
        answer = max(answer, A_accumulated_sum[target] - value)
    else:
        answer = max(answer, A_accumulated_sum[target - 1] - value)
print(f"{answer}")
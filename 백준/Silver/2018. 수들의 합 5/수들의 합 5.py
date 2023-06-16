# 2018 수들의 합 5

from bisect import bisect_left

N = int(input())
answer = 0
sum_to_N = [i * (i + 1) // 2 for i in range(N + 1)]
for index, value in enumerate(sum_to_N):
    target_index = bisect_left(sum_to_N, N + value)
    if target_index == len(sum_to_N):
        break
    if sum_to_N[target_index] - value == N:
        answer += 1
print(answer)
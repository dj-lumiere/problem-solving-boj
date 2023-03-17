# 10986 나머지 합

N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
accumulated_sum_list = [0]
remainder_list = [0 for _ in range(M)]
answer = 0
for i, j in enumerate(A):
    value = (accumulated_sum_list[-1] + j)%M
    accumulated_sum_list.append(value)
    if not value:
        answer += 1
    answer += remainder_list[value]
    remainder_list[value] += 1
print(answer)
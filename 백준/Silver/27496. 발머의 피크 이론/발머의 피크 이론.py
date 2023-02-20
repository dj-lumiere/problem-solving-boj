# C번 - 발머의 피크 이론

from sys import stdin

N, L = list(map(int, stdin.readline().rstrip().split(" ")))
c_list = list(map(int, stdin.readline().rstrip().split(" ")))
partial_sum = 0
answer = 0

for i in range(N):
    if i < L:
        partial_sum += c_list[i]
    else:
        partial_sum += c_list[i] - c_list[i - L]
    if 129 <= partial_sum <= 138:
        answer += 1
print(answer)

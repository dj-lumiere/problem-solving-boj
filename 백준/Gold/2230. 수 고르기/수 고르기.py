# 2230 수 고르기

from sys import stdin
from bisect import bisect_left

N, M = map(int, input().split())
x = [int(stdin.readline().strip()) for _ in range(N)]
x.sort()
answer = 10**11
for i, v in enumerate(x):
    target = bisect_left(x, v + M)
    if target == N:
        break
    else:
        answer = min(answer, x[target] - v)
print(answer)

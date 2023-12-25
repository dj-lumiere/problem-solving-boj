# 31000 교환 분배법칙

from itertools import product

answer = 0
N = int(input())
for b, c in product(range(-N, N + 1), repeat=2):
    if b + c == 1 or not (-N <= -(b + c - 1) <= N):
        answer += 1
    else:
        answer += 2
print(answer)
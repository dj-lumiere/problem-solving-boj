# B2번 - 1차원 2048과 쿼리

from sys import stdin
from math import log2

Q = int(input())
A_counter_list: list[int] = [0 for i in range(63)]
for _ in range(Q):
    A = int(stdin.readline().strip())
    if A != 0:
        A_counter_list[int(log2(abs(A)))] += A // abs(A)
    A_sum_list = A_counter_list[:]
    last_valid_number = 0
    for i, j in enumerate(A_sum_list):
        if i != 62:
            if j == 0:
                continue
            if j == 1:
                last_valid_number = 2**i
            else:
                A_sum_list[i], A_sum_list[i + 1] = (
                    A_sum_list[i] % 2,
                    A_sum_list[i] // 2 + A_sum_list[i + 1],
                )
        elif i == 62 and j > 0:
            last_valid_number = 2**62
    print(last_valid_number)
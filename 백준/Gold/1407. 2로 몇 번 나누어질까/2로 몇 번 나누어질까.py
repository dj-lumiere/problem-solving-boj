# 1407 2로 몇 번 나누어질까
from math import log2, floor


def sum_f(N: int) -> int:
    if N == 0:
        return 0
    else:
        divisable_by_pow_2_n_count: list[int] = [
            N // (2**i) - N // (2 ** (i + 1)) for i in range(floor(log2(N)) + 1)
        ]
        return sum([j * 2**i for i, j in enumerate(divisable_by_pow_2_n_count)])


A, B = list(map(int, input().split(" ")))
print(sum_f(B) - sum_f(A - 1))
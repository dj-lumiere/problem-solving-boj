# 1313 합성소수

from bisect import bisect_left
from sys import stdin


def input():
    return stdin.readline().strip()

compoprime_list = [-1, 111, 117, 119, 171, 231, 237, 297, 319, 371, 411, 413, 417, 437, 471, 473, 531, 537, 597, 611, 671, 679, 711, 713, 717, 731, 737, 831, 837, 897, 973, 979, 1131, 1137, 1311, 1313, 1317, 1379, 1797, 1971, 3113, 3131, 3173, 3179, 4197, 4311, 4313, 4317, 4797, 6137, 6179, 7197, 7971, 31373]

T = int(input())
for _ in range(T):
    N = int(input())
    index = bisect_left(compoprime_list, N)
    if index == len(compoprime_list):
        print(compoprime_list[-1])
    elif compoprime_list[index] == N:
        print(compoprime_list[index])
    else:
        print(compoprime_list[index - 1])

"""
전처리 코드
from itertools import product


def get_prime_sieve(limit: int) -> list[bool]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    return is_prime


compoprime_list = []
prime_list = get_prime_sieve(10**7)
for i in range(3, 8):
    for digit_list in product(range(10), repeat=i):
        if digit_list[0] == 0:
            continue
        current_number = sum([10**i * v for i, v in enumerate(reversed(digit_list))])
        if prime_list[current_number]:
            continue
        subnumbers = []
        for start, end in product(range(i + 1), range(i + 1)):
            if end - start < 2:
                continue
            if start == 0 and end == i:
                continue
            number = sum(
                [
                    10 ** (i - start) * v
                    for i, v in enumerate(reversed(digit_list))
                    if start <= i < end
                ]
            )
            subnumbers.append(number)
        print(current_number, subnumbers)
        if all([prime_list[i] for i in subnumbers]):
            compoprime_list.append(current_number)
print(compoprime_list)
"""
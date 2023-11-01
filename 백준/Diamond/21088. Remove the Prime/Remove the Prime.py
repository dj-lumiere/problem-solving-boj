# 21088 Remove the Prime

from math import gcd
from random import randint
from sys import setrecursionlimit
from collections import Counter

setrecursionlimit(10000)


def next_iteration(x: int, n: int, random_number) -> int:
    return (pow(x, 2, n) + random_number + n) % n


def is_composite(n, power_of_two, remainder, base):
    temp_base = pow(base, remainder, n)
    if temp_base == 1 or temp_base == n - 1:
        return False
    for _ in range(power_of_two - 1):
        temp_base = pow(temp_base, 2, n)
        if temp_base == n - 1:
            return False
    return True


def is_prime(n: int, base_prime_list: list[int]):
    if n in base_prime_list:
        return True
    if n == 1 or n % 2 == 0:
        return False
    power_of_two, remainder = 0, n - 1
    while remainder % 2 == 0:
        remainder //= 2
        power_of_two += 1
    for base in base_prime_list:
        if is_composite(n, power_of_two, remainder, base):
            return False
    return True


def find_single_prime_factor(n: int, base_prime_list: list[int]) -> int:
    if is_prime(n, base_prime_list):
        return n
    if n % 2 == 0:
        return 2
    if n == 1:
        return 1
    x = randint(2, n - 1)
    y = x
    random_number = randint(1, n - 1)
    gcd_value = 1
    while gcd_value == 1:
        x = next_iteration(x, n, random_number)
        y = next_iteration(y, n, random_number)
        y = next_iteration(y, n, random_number)
        gcd_value = gcd(abs(x - y), n)
        if gcd_value == n:
            return find_single_prime_factor(n)
    if is_prime(gcd_value, base_prime_list):
        return gcd_value
    return find_single_prime_factor(gcd_value, base_prime_list)


base_prime_list_for_small = [2, 7, 61]
base_prime_list_for_large = [2, 3, 5, 7, 11, 13, 17, 19, 23]
N = int(input())
numbers = list(map(int, input().split(" ")))
answer = 0
all_factors = set()
for n in numbers:
    next_N = n
    factors = []
    base_prime_list = (
        base_prime_list_for_large if n >= 4_759_123_141 else base_prime_list_for_small
    )
    for i in base_prime_list:
        while next_N % i == 0:
            factors.append(i)
            next_N //= i
    while next_N > 1:
        factor = find_single_prime_factor(next_N, base_prime_list)
        factors.append(factor)
        next_N //= factor
    for k, v in Counter(factors).items():
        all_factors.add(k)

# 같은 소인수를 같은 세그먼트를 돌덩이 1개로 취급.
# grundy_number_list = {}
for factor in all_factors:
    # grundy_number_list[factor] = []
    grundy_number = 0
    for v in numbers:
        if v % factor == 0:
            grundy_number += 1
        else:
            # grundy_number_list[factor].append(grundy_number)
            answer ^= grundy_number
            grundy_number = 0
    #    grundy_number_list[factor].append(grundy_number)
    answer ^= grundy_number
#    grundy_number = 0
# print(grundy_number_list)

# nimber가 0이면 후공 필승
print("First" if answer else "Second")

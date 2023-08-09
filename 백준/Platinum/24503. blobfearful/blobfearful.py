# 24503 blobfearful

from math import gcd
from random import randint
from sys import setrecursionlimit
from collections import Counter

setrecursionlimit(10000)
base_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]


def next_iteration(x: int, n: int, random_number: int) -> int:
    return (pow(x, 2, n) + random_number) % n


def is_composite(n, power_of_two, remainder, base):
    temp_base = pow(base, remainder, n)
    if temp_base == 1 or temp_base == n - 1:
        return False
    for _ in range(power_of_two - 1):
        temp_base = pow(temp_base, 2, n)
        if temp_base == n - 1:
            return False
    return True


def is_prime(n: int):
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


def find_single_prime_factor(n: int) -> int:
    if is_prime(n):
        return n
    if n % 2 == 0:
        return 2
    if n == 1:
        return 1
    x = randint(2, n - 1)
    y = x
    random_number = randint(1, n - 1)
    gcd_value = 1
    iteration = 0
    while gcd_value == 1:
        iteration += 1
        x = next_iteration(x, n, random_number)
        y = next_iteration(y, n, random_number)
        y = next_iteration(y, n, random_number)
        gcd_value = gcd(abs(x - y), n)
        if gcd_value == n:
            return find_single_prime_factor(n)
    if is_prime(gcd_value):
        return gcd_value
    return find_single_prime_factor(gcd_value)


def factorize_large_number(N: int) -> dict[int, int]:
    temp_N = N
    factors = []
    for prime in base_prime_list:
        while temp_N % prime == 0:
            factors.append(prime)
            temp_N //= prime
    while temp_N > 1:
        factor = find_single_prime_factor(temp_N)
        factors.append(factor)
        temp_N //= factor
    return Counter(factors)


K, Q = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
K_factorized = factorize_large_number(K)
K_factor_list = [i for i, _ in K_factorized.items()]
K_multiplier = [v for _, v in K_factorized.items()]


def factorize_n_factorial(n: int) -> list[int]:
    result = [0] * len(K_factor_list)
    for i, v in enumerate(K_factor_list):
        next_n = n
        while next_n > 0:
            result[i] += next_n // v
            next_n //= v
    return result


def factorize_k(k: int) -> list[int]:
    result = [0] * len(K_factor_list)
    for i, v in enumerate(K_factor_list):
        while not k % v:
            result[i] += 1
            k //= v
    return result


def find_blobunfearful_day_base():
    start = 0
    end = K + 1
    while start + 1 < end:
        mid = (start + end) // 2
        mid_fact = factorize_n_factorial(mid)
        is_divisible = True
        for v1, v2 in zip(mid_fact, K_multiplier):
            if v1 < v2:
                is_divisible = False
                break
        if is_divisible:
            end = mid
        else:
            start = mid
    return end


def find_blobunfearful_day(initial_value: int, base: int):
    initial_value_factorized = factorize_k(initial_value)
    start = 0
    end = base + 1
    while start + 1 < end:
        mid = (start + end) // 2
        mid_fact = factorize_n_factorial(mid)
        is_divisible = True
        for i, v in enumerate(initial_value_factorized):
            mid_fact[i] += v
        for v1, v2 in zip(mid_fact, K_multiplier):
            if v1 < v2:
                is_divisible = False
                break
        if is_divisible:
            end = mid
        else:
            start = mid
    return end


base = find_blobunfearful_day_base()
answer = [find_blobunfearful_day(v, base) if v != 1 else base for v in A]
print(" ".join(map(str, answer)))
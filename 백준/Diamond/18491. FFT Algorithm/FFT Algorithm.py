# 18491 FFT Algorithm

from math import gcd, lcm
from random import randint
from sys import setrecursionlimit
from collections import Counter

setrecursionlimit(10000)


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
    base_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
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


def find_all_prime_factors(N: int) -> list[int]:
    temp_N = N
    factors = []
    base_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in base_prime_list:
        while temp_N % prime == 0:
            factors.append(prime)
            temp_N //= prime
    while temp_N > 1:
        factor = find_single_prime_factor(temp_N)
        factors.append(factor)
        temp_N //= factor
    return list(set(factors))


def factorize_large_number(N: int) -> dict[int, int]:
    temp_N = N
    factors = []
    base_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in base_prime_list:
        while temp_N % prime == 0:
            factors.append(prime)
            temp_N //= prime
    while temp_N > 1:
        factor = find_single_prime_factor(temp_N)
        factors.append(factor)
        temp_N //= factor
    return Counter(factors)


def euler_phi(N: int, factors: list[int]) -> int:
    euler_phi = N
    for i in factors:
        euler_phi *= i - 1
        euler_phi //= i
    return euler_phi


def carmichael_lambda(factorization: dict[int, int]):
    result = []
    for k, v in factorization.items():
        if k == 2 and v >= 3:
            result.append(k ** (v - 1) * (k - 1) // 2)
        else:
            result.append(k ** (v - 1) * (k - 1))
    return lcm(*result)


def find_primitive_root(m: int, k: int, factorization: dict[int, int]):
    order = carmichael_lambda(factorization)
    factors = find_all_prime_factors(order)
    if ((order >> k) << k) != order:
        return -1
    pick = 2
    result = 1
    while True:
        pick = randint(2, m - 1)
        if gcd(pick, m) != 1:
            continue
        if pow(pick, order, m) == 1 and all(
            pow(pick, order // i, m) != 1 for i in factors
        ):
            result = pow(pick, (order >> k), m)
            break
    return result


m, k = map(int, input().split(" "))
factorization = factorize_large_number(m)
print(find_primitive_root(m, k, factorization))

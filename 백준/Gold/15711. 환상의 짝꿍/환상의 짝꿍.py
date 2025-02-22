from collections import Counter
from math import gcd
from random import randint
from sys import setrecursionlimit
from sys import stderr, stdout

# 큰 수의 소수 판정 및 소인수분해 코드

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
    base_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
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
    base_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
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
    base_prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for prime in base_prime_list:
        while temp_N % prime == 0:
            factors.append(prime)
            temp_N //= prime
    while temp_N > 1:
        factor = find_single_prime_factor(temp_N)
        factors.append(factor)
        temp_N //= factor
    return Counter(factors)


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(t):
        answer = "NO"
        a, b = int(input()), int(input())
        if a + b == 2:
            answer = "NO"
        elif a + b == 3:
            answer = "NO"
        elif (a + b) % 2 == 0:
            answer = "YES"
        else:
            if is_prime(a + b - 2):
                answer = "YES"
            else:
                answer = "NO"
        answers.append(answer)
    print(*answers, sep="\n")
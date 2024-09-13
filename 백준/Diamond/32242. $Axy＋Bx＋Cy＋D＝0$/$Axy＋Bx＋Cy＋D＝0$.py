from bisect import bisect_left, bisect_right
from string import ascii_uppercase, ascii_lowercase
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit, stdout, stderr
from random import randint, shuffle
from collections import deque, Counter
from math import log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop, heapify
from itertools import combinations, pairwise, permutations, combinations_with_replacement, product, zip_longest, chain, groupby
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000
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
    if N == 0 or N == 1:
        return {}
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


def extended_euclidean(a: int, b: int, d: int) -> int:
    if d % gcd(a, b) != 0:
        return 0
    return 1


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        a, b, c, d = (int(input()) for _ in range(4))
        if a == 0 and b == 0 and c == 0 and d != 0:
            answer = "0"
        elif a == 0 and b == 0 and c == 0 and d == 0:
            answer = "INFINITY"
        elif a == 0 and b == 0 and d % c:
            answer = "0"
        elif a == 0 and b == 0 and d % c == 0:
            answer = "INFINITY"
        elif a == 0 and c == 0 and d % b:
            answer = "0"
        elif a == 0 and c == 0 and d % b == 0:
            answer = "INFINITY"
        elif a != 0 and b == 0 and c == 0 and d == 0:
            answer = "INFINITY"
        elif a == 0:
            if extended_euclidean(b, c, d) == 1:
                answer = "INFINITY"
            else:
                answer = "0"
        else:
            if a < 0:
                a, b, c, d = -a, -b, -c, -d
            det = b * c - a * d
            if det == 0:
                answer = "INFINITY" if b%a==0 or c%a==0 else "0"
            else:
            #eprint(det)
                factorize = factorize_large_number(abs(det))
            #eprint(factorize)
                possible_answers = []
                for factors in product(*([(k, i) for i in range(v + 1)] for k, v in factorize.items())):
                    current = 1
                    for k, v in factors:
                        current *= k ** v
                    possible_answers.extend([(current, det // current), (-current, -det // current)])
            #eprint(possible_answers)
                real_answer = []
                for i, j in possible_answers:
                    if (i - c) % a == 0 and (j - b) % a == 0:
                        real_answer.append(((i - c) // a, (j - b) // a))
                real_answer = sorted(set(real_answer))
            #eprint(real_answer)
                answer = f"{len(real_answer)}\n" + "\n".join(f"{a} {b}" for a, b in real_answer)
        answers.append(f"{answer}")
print(*answers, sep="\n")
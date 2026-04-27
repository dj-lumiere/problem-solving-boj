from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
from heapq import heappush, heappop
from itertools import combinations, permutations, combinations_with_replacement, product, zip_longest
from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache, reduce
import re

getcontext().prec = 1000


def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(is_prime) if v]


def get_prime_factors(value: int, primes: list[int]) -> list[int]:
    prime_factors = []
    for i in primes:
        if i * i > value:
            break
        if value % i:
            continue
        while value % i == 0:
            prime_factors.append(i)
            value //= i
    if value != 1:
        prime_factors.append(value)
    return prime_factors


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    primes = extract_primes_from_sieve(1000)
    for h in range(t):
        n = int(input())
        answer = 0
        for i in range(1, n + 1):
            prime_factors = set(get_prime_factors(i, primes))
            phi = i
            for j in prime_factors:
                phi *= j - 1
                phi //= j
            answer += phi
        answers[h] = f"{answer * 2 + 1}"
    print(answers)
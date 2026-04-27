from bisect import bisect_left
from time import perf_counter_ns, sleep
from datetime import datetime, timedelta
from sys import setrecursionlimit
from os import write
from random import randint, shuffle
from collections import deque, Counter
from math import comb, lcm, log, gcd, floor, log2, log10, pi, ceil, factorial, sqrt
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


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: write(1, "\n".join(x).encode())
    eprint = lambda *args, **sep: write(2, (" ".join(map(str, args)) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    MOD = 998244353
    for hh in range(t):
        pass
    primes = extract_primes_from_sieve(10000)
    while True:
        try:
            n = int(input())
            factors = [0 for _ in primes]
            answer = 1
            for i, v in enumerate(primes):
                next_n = n
                while next_n > 0:
                    factors[i] += next_n // v
                    next_n = next_n // v
            factors[0] -= factors[2]
            factors[2] -= factors[2]
            for i, v in enumerate(primes):
                answer *= pow(v, factors[i], 10)
                answer %= 10
            answers.append(f"{n} -> {answer}")
        except:
            break
    maxlen = max(map(len, answers))
    for i, v in enumerate(answers):
        answers[i] = " " * (maxlen - len(v) + 1) + v
    print(answers)
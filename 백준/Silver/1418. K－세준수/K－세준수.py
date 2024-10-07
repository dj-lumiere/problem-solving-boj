from collections import deque, Counter
from itertools import product, chain, permutations, combinations, repeat
from string import ascii_lowercase
from sys import stdout, stderr
from time import perf_counter
from decimal import Decimal
from math import isqrt
from heapq import heappush, heappop


def get_prime_sieve(limit):
    result = [False, False] + [True for _ in range(limit - 1)]
    for i in range(2, limit + 1):
        if not result[i]:
            continue
        for j in range(2, limit + 1):
            if i * j >= limit + 1:
                break
            result[i * j] = False
    return result


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
    T = 1
    answers = []
    for hh in range(1, T + 1):
        N = int(input())
        K = int(input())
        sejun_count = [i for i in range(N + 1)]
        sejun_count[0] = 0
        primes = get_prime_sieve(K)
        for i in range(2, N + 1):
            for j, v in enumerate(primes):
                if not v:
                    continue
                while sejun_count[i] % j == 0:
                    sejun_count[i] //= j
        result = 0
        for i in range(1, N + 1):
            if sejun_count[i] == 1:
                result += 1
        answers.append(result)
    print(*answers, sep="\n")

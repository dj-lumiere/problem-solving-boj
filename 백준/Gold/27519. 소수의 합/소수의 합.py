# 27519 소수의 합
from itertools import product
from sys import stdin

MOD = 1000000007


def input():
    return stdin.readline().strip()


def extract_primes_from_sieve(limit: int) -> list[int]:
    prime_flags = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not prime_flags[i]:
            continue
        prime_flags[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(prime_flags) if v]


limit = 100000
prime_list = extract_primes_from_sieve(limit)
result = [0 for _ in range(limit + 1)]
result[0] = 1
for prime in prime_list:
    for i in range(prime, limit + 1):
        result[i] += result[i - prime]
        result[i] %= MOD

T = int(input())
for _ in range(T):
    n = int(input())
    print(result[n])
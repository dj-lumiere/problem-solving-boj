# 11790 Primorial vs LCM

from bisect import bisect_right
from sys import stdin


def input():
    return stdin.readline().strip()


def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(is_prime) if v]


MOD = 1000000007
prime_list = extract_primes_from_sieve(10**7 + 1)
prime_list_multiply = [1]
for i, v in enumerate(prime_list):
    prime_list_multiply.append(v * prime_list_multiply[-1] % MOD)

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    j = 2
    answer = 1
    while True:
        index = bisect_right(prime_list, round(N ** (1 / j), 10))
        if index == 0:
            break
        answer *= prime_list_multiply[index]
        answer %= MOD
        j += 1
    print(f"Case {i}: {answer}")
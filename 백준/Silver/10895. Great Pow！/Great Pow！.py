# 10895 Great Pow!
from sys import stdin


def input():
    return stdin.readline().strip()


def extract_primes_from_sieve(limit: int) -> list[int]:
    prime_flags = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not prime_flags[i]:
            continue
        prime_flags[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(prime_flags) if v]


def euler_phi(prime_list: list[int], M: int):
    if M == 1:
        return 1
    factor_list = []
    result = M
    next_M = M
    for i in prime_list:
        if i * i > M:
            break
        if M % i == 0:
            factor_list.append(i)
            next_M //= i
            while next_M % i == 0:
                next_M //= i
    for i in factor_list:
        result = result * (i - 1) // i
    if next_M != 1 and next_M not in factor_list:
        result = result * (next_M - 1) // next_M
    return result


def power_tower(prime_list: list[int], element: int, index: int, MOD: int):
    if MOD == 1:
        return 1
    if index == 0:
        return 1
    if element % MOD == 0:
        return 0
    euler_phi_mod = euler_phi(prime_list, MOD)
    sub_result = power_tower(prime_list, element, index - 1, euler_phi_mod)
    return pow(element, sub_result, MOD)


prime_list = extract_primes_from_sieve(int(10**4.5) + 1)
global is_excessive_at_next
is_excessive_at_next = False
a, k = map(int, input().split(" "))
if a == 1:
    print(1)
else:
    print(power_tower(prime_list, a, k + 1, a + 1) % (a + 1))
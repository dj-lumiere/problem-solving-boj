# 16214 N과 M
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


def is_excessive(base: int, exp: int, threshold: int):
    result = 1
    while exp:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
        if result >= threshold:
            return True
    return False


def power_tower(prime_list: list[int], element: int, MOD: int):
    global is_excessive_at_next
    if MOD == 1:
        return 1
    if element % MOD == 0:
        return 0
    euler_phi_mod = euler_phi(prime_list, MOD)
    sub_result = power_tower(prime_list, element, euler_phi_mod)
    base, exp = element, sub_result
    if is_excessive_at_next:
        exp += euler_phi_mod
    # print(f"{index=} {MOD=} {tower[index:]=} {base=} {exp=} {is_excessive(base, exp, MOD)=}")
    if not is_excessive_at_next:
        is_excessive_at_next = is_excessive(base, exp, MOD)
    return pow(base, exp, MOD)


prime_list = extract_primes_from_sieve(int(10**4.5) + 1)
global is_excessive_at_next
is_excessive_at_next = False
T = int(input())
for _ in range(T):
    N, M = map(int, input().split(" "))
    is_excessive_at_next = False
    print(power_tower(prime_list, N, M) % M)
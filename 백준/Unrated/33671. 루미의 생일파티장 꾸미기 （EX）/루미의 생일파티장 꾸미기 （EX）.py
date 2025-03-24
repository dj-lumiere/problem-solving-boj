from heapq import heappop, heappush
from sys import stderr, stdout
from math import gcd
from random import randint
from sys import setrecursionlimit
from collections import Counter

PRECOMPUTE_LIMIT = 1_600_000
PHI_PRECOMPUTE = [i for i in range(PRECOMPUTE_LIMIT)]
PHI_LARGE = {}
PHI_SUM_PRECOMPUTE = [0 for i in range(PRECOMPUTE_LIMIT)]
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


def precompute_phi():
    for i in range(2, PRECOMPUTE_LIMIT):
        if PHI_PRECOMPUTE[i] != i:
            continue
        for j in range(i, PRECOMPUTE_LIMIT, i):
            PHI_PRECOMPUTE[j] *= (i - 1)
            PHI_PRECOMPUTE[j] //= i
    for i in range(1, PRECOMPUTE_LIMIT):
        PHI_SUM_PRECOMPUTE[i] = (PHI_SUM_PRECOMPUTE[i - 1] + PHI_PRECOMPUTE[i]) % MOD


def compute_phi(x):
    if x < PRECOMPUTE_LIMIT:
        return PHI_SUM_PRECOMPUTE[x]
    if x in PHI_LARGE:
        return PHI_LARGE[x]
    result = (x * (x + 1) // 2) % MOD
    i = 2
    while i <= x:
        j = x // (x // i)
        result -= (j - i + 1) * compute_phi(x // i)
        result %= MOD
        i = j + 1
    PHI_LARGE[x] = result
    return result


MOD = 998_244_353
n, l = map(int, input().split())
prime_factors = find_all_prime_factors(l)
phi_l = l

for prime_factor in prime_factors:
    phi_l *= (prime_factor - 1)
    phi_l //= prime_factor

heap = prime_factors[:]
special_numbers_set = set(prime_factors)
while heap:
    next_n = heappop(heap)
    for i in prime_factors:
        if next_n * i in special_numbers_set:
            continue
        if next_n * i > n:
            break
        special_numbers_set.add(next_n * i)
        heappush(heap, next_n * i)
special_numbers_set.add(1)

precompute_phi()
compute_phi(n)

answer = 0
for x in special_numbers_set:
    answer += compute_phi(n // x)
    answer %= MOD
answer *= phi_l
answer %= MOD

print(answer, sep="\n")
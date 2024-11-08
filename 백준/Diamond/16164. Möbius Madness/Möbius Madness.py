from bisect import bisect_right
from collections import Counter
from heapq import heappop, heappush
from math import gcd
from random import randint
from sys import setrecursionlimit
from sys import stderr, stdout

MOD = 10 ** 9 + 7
INV_2 = 500000004
PRECOMPUTE_LIMIT = 100000

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


def sum_of_mu_l(x, sum_small, sum_big, special_numbers):
    i, j = 2, 0
    if x <= PRECOMPUTE_LIMIT:
        return sum_small[x]
    if x in sum_big:
        return sum_big[x]
    result = bisect_right(special_numbers, x)
    while i <= x:
        j = x // (x // i)
        result -= (j - i + 1) * sum_of_mu_l(x // i, sum_small, sum_big, special_numbers)
        i = j + 1
    sum_big[x] = result
    return result


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
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n, l, k = (int(input()) for _ in range(3))
        l_factorize = factorize_large_number(l)

        if any(v > 1 for v in l_factorize.values()):
            answers.append(0)
            continue
        mu_l = (-1) ** len(l_factorize)

        keys = [v for v in l_factorize.keys()]
        if keys:
            special_numbers_set = set([1])
            heap = [1]

            smallest_key = min(keys)
            while heap:
                x = heappop(heap)
                for i in keys:
                    if x * i > n:
                        continue
                    if x * i in special_numbers_set:
                        continue
                    special_numbers_set.add(x * i)
                    heappush(heap, x * i)
            for i in heap:
                special_numbers_set.add(i)
        else:
            special_numbers_set = set()

        special_numbers = sorted(special_numbers_set)
        mu_i_small = [1 for _ in range(PRECOMPUTE_LIMIT + 1)]
        mu_i_small[0] = 0
        done_calculating = [0 for _ in range(PRECOMPUTE_LIMIT + 1)]
        sum_small = [0 for _ in range(PRECOMPUTE_LIMIT + 1)]
        sum_big = {}

        for i in range(2, PRECOMPUTE_LIMIT + 1):
            if not done_calculating[i]:
                for j in range(i, PRECOMPUTE_LIMIT + 1, i):
                    mu_i_small[j] *= -1
                    done_calculating[j] = True
                for j in range(i * i, PRECOMPUTE_LIMIT + 1, i * i):
                    mu_i_small[j] = 0

        mu_l_i_small = mu_i_small[:]
        for i in range(2, PRECOMPUTE_LIMIT + 1):
            if gcd(i, l) != 1:
                mu_l_i_small[i] = 0

        for i in range(1, PRECOMPUTE_LIMIT + 1):
            sum_small[i] = sum_small[i - 1] + mu_l_i_small[i]

        n_over_ds = []
        lower_bound = []
        upper_bound = []
        for i in range(1, int(n ** .5) + 1):
            n_over_ds.append(i)
            n_over_ds.append(n // i)
        n_over_ds = sorted(set(n_over_ds))
        for i, j in zip(n_over_ds, n_over_ds[1:]):
            lower_bound.append(i + 1)
            upper_bound.append(j)
        lower_bound.reverse()
        upper_bound.reverse()
        lower_bound.append(1)
        upper_bound.append(1)
        sum_upper_bound = [sum_of_mu_l(v, sum_small, sum_big, special_numbers) for v in reversed(upper_bound)]
        sum_lower_bound = [sum_of_mu_l(v - 1, sum_small, sum_big, special_numbers) for v in reversed(lower_bound)]

        sum_upper_bound.reverse()
        sum_lower_bound.reverse()
        auxilary_terms = [pow(v, k, MOD) for v in n_over_ds]

        answer = mu_l * sum(v * (r - l) % MOD for v, l, r in zip(auxilary_terms, sum_lower_bound, sum_upper_bound))
        answer %= MOD
        answers.append(f"{answer}")
    print(*answers, sep="\n")
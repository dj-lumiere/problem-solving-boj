# 2824 최대공약수
from collections import Counter


def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
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


def factorize(value: int, prime_list: list[int]) -> dict[int, int]:
    prime_factors = get_prime_factors(value, prime_list)
    factorized_dict = Counter(prime_factors)
    return factorized_dict


_ = int(input())
A = list(map(int, input().split(" ")))
_ = int(input())
B = list(map(int, input().split(" ")))
prime_list = extract_primes_from_sieve(int(10**4.5) + 1)
A_product = {}
for i in A:
    i_factorized = factorize(i, prime_list)
    for k, v in i_factorized.items():
        if k not in A_product:
            A_product[k] = v
            continue
        A_product[k] += v
B_product = {}
for i in B:
    i_factorized = factorize(i, prime_list)
    for k, v in i_factorized.items():
        if k not in B_product:
            B_product[k] = v
            continue
        B_product[k] += v
intersect = {}
for k, v in A_product.items():
    if k in B_product:
        intersect[k] = min(v, B_product[k])
result = 1
is_over_1_000_000_000 = False
for k, v in intersect.items():
    result *= pow(k, v, 1_000_000_000)
    if pow(k, v, 1_000_000_000) != pow(k, v, 1_000_000_001):
        is_over_1_000_000_000 = True
    if result >= 1_000_000_000:
        is_over_1_000_000_000 = True
        result %= 1_000_000_000
result %= 1_000_000_000
print(f"{result:0>9}" if is_over_1_000_000_000 else f"{result}")
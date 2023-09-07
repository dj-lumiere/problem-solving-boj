# 28474 피보나치 서로소


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
    return list(set(prime_factors))


def euler_phi(value: int, prime_list: list[int]) -> int:
    prime_factors = get_prime_factors(value, prime_list)
    result = value
    for prime in prime_factors:
        result = result * (prime - 1) // prime
    return result


def sol(n: int, prime_list: list[int]) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    result = euler_phi(n, prime_list)
    if n % 2 == 0:
        result += euler_phi(n // 2, prime_list)
    return result


prime_list = extract_primes_from_sieve(int(10**4.5) + 1)
n = int(input())
for _ in range(n):
    target = int(input())
    print(sol(target, prime_list))
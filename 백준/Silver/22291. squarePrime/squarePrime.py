def get_prime_sieve(limit: int) -> list[bool]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return is_prime


def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(is_prime) if v]


primes = get_prime_sieve(100001)


def isPrime(n):
    return primes[n]


def isSquare(n):
    return 0 <= n == int(n ** .5) ** 2


def P2(A):
    n = len(A)
    # ADD ADDITIONAL CODE HERE!
    return sum(v for i, v in enumerate(A) if isPrime(i) and isSquare(v))
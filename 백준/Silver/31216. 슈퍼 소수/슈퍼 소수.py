# B번 - 슈퍼 소수


def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(is_prime) if v]


primes = extract_primes_from_sieve(10**6)
super_primes = [0]
for i in range(3000):
    super_primes.append(primes[primes[i] - 1])
T = int(input())
for _ in range(T):
    N = int(input())
    print(super_primes[N])
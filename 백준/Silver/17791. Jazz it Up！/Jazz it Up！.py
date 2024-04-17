import os


def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
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


def factorize(value: int, prime_list) -> dict[int, int]:
    prime_factors = get_prime_factors(value, prime_list)
    factorized_dict = dict()
    for factor in prime_factors:
        factorized_dict[factor] = factorized_dict.get(factor, 0) + 1
    return factorized_dict


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    primes = extract_primes_from_sieve(200000)
    prime_set = set(primes)
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        factorize_n = factorize(n, primes)
        answer = 1
        for v in primes:
            if v not in factorize_n:
                answer = v
                break
        answers[h] = f"{answer}"
    print(answers)
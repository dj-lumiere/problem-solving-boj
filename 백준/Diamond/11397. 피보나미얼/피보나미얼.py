# 11397 피보나미얼
# 피사노 주기 이용 : π(p**k) divides p**k–1*π(p) (원래는 =은 아니지만, 2**64까지는 =로 봐도 된다.)
# If m and n are coprime, then π(mn) is the least common multiple of π(m) and π(n), by the Chinese remainder theorem


def extract_primes_from_sieve(limit: int) -> list[int]:
    if limit <= 0:
        return []
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


def factorize(value: int) -> dict[int, int]:
    prime_list = extract_primes_from_sieve(value)
    prime_factors = get_prime_factors(value, prime_list)
    factorized_dict = dict()
    for factor in prime_factors:
        factorized_dict[factor] = factorized_dict.get(factor, 0) + 1
    return factorized_dict


n, p = map(int, input().split(" "))

prime_list = extract_primes_from_sieve(1000)
zero_period = []
for i in prime_list:
    fib = [0, 1]
    for j in range(10000):
        fib_sub = sum(fib[-2:]) % i
        if fib_sub == 0:
            zero_period.append(j + 2)
            break
        fib.append(fib_sub)

fibonamial_factorization = [0] * len(prime_list)
for i, v in enumerate(prime_list):
    next_v = v
    next_period = zero_period[i]
    while next_period <= n:
        if next_v == 8:
            next_period = 6
        fibonamial_factorization[i] += n // next_period
        next_v *= v
        next_period *= v

for i in range(2, p + 1):
    i_factorization = factorize(i)
    result = 2**63
    for j, v in enumerate(prime_list):
        if v not in i_factorization:
            continue
        result = min(result, fibonamial_factorization[j] // i_factorization[v])
    print(result)

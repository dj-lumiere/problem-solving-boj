def get_prime_sieve(limit):
    result = [False, False] + [True for _ in range(limit-1)]
    for i in range(2, limit+1):
        if not result[i]:
            continue
        for j in range(2, limit+1):
            if i*j >= limit+1:
                break
            result[i*j] = False
    return result

prime_sieve = get_prime_sieve(1000)
primes = [i for i, v in enumerate(prime_sieve) if v]
underprimes = [False for _ in range(100001)]
for i in range(2, 100001):
    factors = []
    i2 = i
    while True:
        for v in primes:
            if i2 % v == 0:
                factors.append(v)
                i2 //= v
                break
        else:
            break
    if i2 != 1:
        factors.append(i2)
    if prime_sieve[len(factors)]:
        underprimes[i] = True
a, b = map(int, input().split())
print(sum(underprimes[a:b+1]))
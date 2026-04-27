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


prime_sieve = get_prime_sieve(1300000)
primes = [i for i, v in enumerate(prime_sieve) if v]
palindrome_primes = [i for i in primes if str(i) == str(i)[::-1]]
n = int(input())
for i, j in zip(palindrome_primes, palindrome_primes[1:]):
    if n <= i:
        print(i)
        break
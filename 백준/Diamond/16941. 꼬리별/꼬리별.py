from sys import stderr, stdout


def get_prime_sieve(limit):
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return is_prime


def powered_sum(n, d, smaller_sum, MOD):
    if n <= d + 2:
        return smaller_sum[n]
    if n == MOD:
        return (powered_sum(n - 1, d, smaller_sum, MOD) + pow(n, d, MOD)) % MOD
    numerator_accumulate[0] = n
    for i in range(1, d + 3):
        numerator_accumulate[i] = numerator_accumulate[i - 1] * (n - i) % MOD
    numerator_inverse[0] = pow(numerator_accumulate[-1], MOD-2, MOD)
    j = 1
    for i in reversed(range(1, d + 3)):
        numerator_inverse[j] = numerator_inverse[j - 1] * (n - i) % MOD
        j += 1
    numerator_inverse.reverse()
    numerator_sub_inverse = [i * j % MOD for i, j in zip(numerator_accumulate, numerator_inverse[1:])]
    numerators = [(numerator_accumulate[-1] * numerator_inverse[0]) % MOD * v % MOD for v in numerator_sub_inverse]
    coefficients = [i * j % MOD for i, j in zip(numerators, denominators)]
    return sum(i * j % MOD for i, j in zip(coefficients, smaller_sum[1:])) % MOD


with open(0, "r") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    # MOD = 1_000_000_007
    t = 1
    answers = []
    limit = int(10 ** 4.5) + 1
    primes = get_prime_sieve(limit)
    for hh in range(1, t + 1):
        n = int(input())
        q = int(input())
        m = int(n ** .5)
        prime_count = [0 for _ in range(limit)]
        smaller_powers = [pow(i, q, n) for i in range(limit)]
        for i in range(1, limit):
            prime_count[i] = (prime_count[i - 1] + primes[i] * smaller_powers[i] % n) % n
        if n < limit:
            answers.append(prime_count[n])
            continue
        denominator_sub = list(range(-q - 1, 0)) + list(range(1, q + 2))
        denominator_accumulate = [1]
        for v in denominator_sub:
            denominator_accumulate.append(denominator_accumulate[-1] * v % n)
        denominator_accumulate_inverse = [pow(denominator_accumulate[-1], n-2, n)]
        for i, v in enumerate(reversed(denominator_sub)):
            denominator_accumulate_inverse.append(denominator_accumulate_inverse[-1] * v % n)
        denominator_accumulate_inverse.reverse()
        denominators = [i * j % n for i, j in zip(denominator_accumulate, denominator_accumulate_inverse[q + 1:])]
        numerator_accumulate = [n for _ in range(q + 3)]
        numerator_inverse = [n for _ in range(q + 3)]
        smaller_sum = [0]
        for i in range(1, limit + 3):
            smaller_sum.append((smaller_sum[-1] + pow(i, q, n)) % n)
        dp = (
                [0]
                + list(map(lambda _: (_ - 1) % n, smaller_sum[1:m + 1]))
                + [(powered_sum(n // v, q, smaller_sum, n) - 1) % n for v in reversed(range(1, m + 1))]
        )

        for i in range(2, m + 1):
            if not primes[i]:
                continue
            for j in range(1, m + 1):
                if n // j < i * i:
                    break
                x = (n // j) // i
                y = dp[-(n // x)] if x > m else dp[x]
                dp[-j] = (dp[-j] - smaller_powers[i] * (y - prime_count[i - 1]) % n) % n
            for j in reversed(range(1, m + 1)):
                if j < i * i:
                    break
                x = j // i
                y = dp[-(n // x)] if x > m else dp[x]
                dp[j] = (dp[j] - smaller_powers[i] * (y - prime_count[i - 1]) % n) % n
        answer = dp[-1]
        answers.append(f"{answer}")
    print(*answers, sep="\n")
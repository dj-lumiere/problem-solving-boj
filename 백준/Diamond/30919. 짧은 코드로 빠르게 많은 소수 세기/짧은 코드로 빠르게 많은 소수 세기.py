from sys import setrecursionlimit, stdout, stderr


def get_prime_sieve(limit):
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return is_prime


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    t = int(input())
    answers = []
    primes = get_prime_sieve(10 ** 6 + 1)
    prime_count = [0 for _ in range(len(primes))]
    for i in range(1, len(primes)):
        prime_count[i] = prime_count[i - 1] + primes[i]
    for hh in range(1, t + 1):
        n = int(input())
        if n <= 10 ** 6:
            answers.append(prime_count[n])
            continue
        m = int(n ** .5)
        dp = [0] + [v - 1 for v in range(1, m + 1)] + [n // v - 1 for v in reversed(range(1, m + 1))]


        def get_dp_value(x):
            if x <= m:
                return dp[x]
            return dp[-(n // x)]


        for i in range(2, m + 1):
            if not primes[i]:
                continue
            for j in range(1, m + 1):
                if n // j < i * i:
                    break
                dp[-j] = dp[-j] - get_dp_value((n // j) // i) + prime_count[i - 1]
            for j in reversed(range(1, m + 1)):
                if j < i * i:
                    break
                dp[j] = dp[j] - get_dp_value(j // i) + prime_count[i - 1]
        answer = get_dp_value(n)
        answers.append(answer)
    print(*answers, sep="\n")

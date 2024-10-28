from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    sieve = [True] * (10 ** 6 + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int((10 ** 6) ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, 10 ** 6 + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    t = int(input())
    answers = []
    for _ in range(t):
        S = int(input())
        is_valid = True
        for p in primes:
            if p * p > S:
                break
            if S % p == 0:
                is_valid = False
                break
        answer = "YES" if is_valid else "NO"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
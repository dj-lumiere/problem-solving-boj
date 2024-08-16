from itertools import product
from sys import stdout, stderr


def primes(n):
    result = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** .5) + 1):
        if not result[i]:
            continue
        for j in range(2 * i, n + 1, i):
            result[j] = False
    return [i for i, v in enumerate(result) if v]


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    prime = primes(118)
    two_prime_sum = set(i + j for i, j in product(prime, repeat=2))
    for hh in range(t):
        x = int(input())
        answer = "Yes" if x in two_prime_sum else "No"
        answers.append(f"{answer}")
    print(*answers, sep="\n")

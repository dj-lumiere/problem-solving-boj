from itertools import product
from sys import stderr, stdout


def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(is_prime) if v]


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    primes_under_1000 = extract_primes_from_sieve(1000)
    pre_calculated_answer = ["" for _ in range(1000)]
    for a, b, c in product(primes_under_1000, primes_under_1000, primes_under_1000):
        if a + b + c >= 1000:
            continue
        if pre_calculated_answer[a + b + c] != "":
            continue
        pre_calculated_answer[a + b + c] = f"{a} {b} {c}"
    answers = []
    for hh in range(t):
        n = int(input())
        answer = pre_calculated_answer[n]
        answers.append(f"{answer}")
    print(*answers, sep="\n")
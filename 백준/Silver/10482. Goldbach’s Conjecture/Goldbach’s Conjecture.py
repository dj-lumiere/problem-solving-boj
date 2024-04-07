import os
from itertools import product


def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit ** 0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2: limit + 1: i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(is_prime) if v]


# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    primes = extract_primes_from_sieve(32001)
    goldbach_partition = [[] for _ in range(32001)]
    for i, j in product(primes, repeat=2):
        if i > j:
            continue
        if i + j >= 32001:
            continue
        goldbach_partition[i + j].append((i, j))
    for v in goldbach_partition:
        v.sort(key=lambda x: x[0])
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        answer = f"{n} has {len(goldbach_partition[n])} representation(s)\n" + "\n".join(map(lambda x: f"{x[0]}+{x[1]}",
                                                                                             goldbach_partition[n]))
        answers[i] = answer
    # while True:
    #     n = int(input())
    #     if n == 0:
    #         break
    #     a = [int(input()) for _ in range(n)]
    #     answers.append("\n".join(map(str, reversed(a)))+"\n0")
    print(answers)
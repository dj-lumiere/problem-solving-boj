import array
import os
from heapq import heappush, heappop

def extract_primes_from_sieve(limit: int) -> list[int]:
    is_prime = [False, False] + [True for _ in range(2, limit + 1)]
    for i in range(2, int(limit**0.5) + 1):
        if not is_prime[i]:
            continue
        is_prime[i * 2 : limit + 1 : i] = [False] * (limit // i - 1)
    return [i for i, v in enumerate(is_prime) if v]

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    primes = extract_primes_from_sieve(20000)
    for i in range(t):
        n = int(input())
        factors = [0 for _ in range(len(primes))]
        answer = 1
        for j, v in enumerate(primes):
            next_n = n
            while next_n != 0:
                next_n //= v
                factors[j] += next_n
        factors[0] -= factors[2]
        factors[2] = 0
        for v1, v2 in zip(primes, factors):
            answer = answer * pow(v1, v2, 10) % 10
        answers[i] = f"{answer}"
    # while True:
    #     n = int(input())
    #     if n == 0:
    #         break
    #     a = [int(input()) for _ in range(n)]
    #     answers.append("\n".join(map(str, reversed(a)))+"\n0")
    print(answers)
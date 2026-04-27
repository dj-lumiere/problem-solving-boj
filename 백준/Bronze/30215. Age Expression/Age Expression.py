import os
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        o = int(input())
        a = int(input())
        b = int(input())
        answer = 0
        for n, m in product(range(1, 151), repeat=2):
            if a * n + b * m == o:
                answer += 1
                break
        answers[h] = f"{answer}"
    print(answers)
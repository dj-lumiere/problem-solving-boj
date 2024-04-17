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
        n = int(input())
        x = [int(input()) for _ in range(n)]
        even = sum(i % 2 == 0 for i in x)
        odd = n - even
        answer_odd = sum(i for i, v in enumerate(x) if v % 2 == 1) - sum(range(odd))
        answer_even = sum(i for i, v in enumerate(x) if v % 2 == 0) - sum(range(even))
        answer = min(answer_even, answer_odd)
        answers[h] = f"{answer}"
    print(answers)
import os
from itertools import permutations

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        numbers = [int(input()) for _ in range(4)]
        answer = max([a * b + c * d for a, b, c, d in permutations(numbers)])
        answers[i] = f"{answer}"
    print(answers)
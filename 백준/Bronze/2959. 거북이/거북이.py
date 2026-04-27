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
        max_area = max([min(i1, i2) * min(j1, j2) for i1, i2, j1, j2 in permutations(numbers, r=4)])
        answers[i] = str(max_area)
    print(answers)
import os
from functools import reduce
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    x = [(0, 1), (1, 1), (1, 2)]
    star = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for i in range(t):
        n = int(input())
        answer = [[" " for _ in range(3 * n)] for _ in range(3 * n)]
        for j, k in x:
            for l, m in product(range(n), repeat=2):
                answer[j * n + l][k * n + m] = "x"
        for j, k in star:
            for l, m in product(range(n), repeat=2):
                answer[j * n + l][k * n + m] = "*"
        answers[i] = "\n".join("".join(i) for i in answer)
    print(answers)
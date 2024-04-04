import os
from itertools import product

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = int(next(tokens))
    answers = ["" for _ in range(t)]
    triangle_numbers = [i * (i + 1) // 2 for i in range(1, 40)]
    possible = [False for _ in range(1001)]
    for j1, j2, j3 in product(triangle_numbers, repeat=3):
        if j1 + j2 + j3 < 1001:
            possible[j1 + j2 + j3] = True
    for i in range(t):
        answer = int(possible[int(next(tokens))])
        answers[i] = str(answer)
    os.write(1, "\n".join(answers).encode())
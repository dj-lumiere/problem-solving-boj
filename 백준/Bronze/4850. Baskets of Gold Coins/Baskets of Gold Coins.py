import os
from itertools import product
from fractions import Fraction

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        pass
    while True:
        try:
            n, w, d, x = [int(input()) for _ in range(4)]
            answer = ((n-1)*n//2*w-x)//d
            if answer == 0:
                answer = n
            answers.append(f"{answer}")
        except:
            break
    print(answers)
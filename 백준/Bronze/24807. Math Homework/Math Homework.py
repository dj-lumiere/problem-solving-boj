import os
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        b,d,c,l = [int(input()) for _ in range(4)]
        answer = []
        for e,f,g in product(range(l+1), repeat=3):
            if e*b+f*d+g*c == l:
                answer.append((e,f,g))
        answer.sort()
        answers[i] = "\n".join(map(lambda x:" ".join(map(str, x)), answer)) if answer else "impossible"
    print(answers)
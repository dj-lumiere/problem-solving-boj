import os
from functools import reduce
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        left = [int(input()) for _ in range(n)]
        right = [int(input()) for _ in range(n)]
        answer = 0
        for j in left:
            if j + 500 in left and j + 1000 in right and j + 1500 in right:
                answer += 1
        answers[i] = f"{answer}"
    print(answers)
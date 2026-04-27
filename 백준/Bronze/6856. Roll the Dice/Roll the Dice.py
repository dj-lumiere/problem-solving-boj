import os
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 10001
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        m = int(input())
        answer = sum(i+j==10 for i, j in product(range(1, n+1), range(1, m+1)))
        if answer == 1:
            answers[h] = f"There is {answer} way to get the sum 10."
        else:
            answers[h] = f"There are {answer} ways to get the sum 10."
    print(answers)
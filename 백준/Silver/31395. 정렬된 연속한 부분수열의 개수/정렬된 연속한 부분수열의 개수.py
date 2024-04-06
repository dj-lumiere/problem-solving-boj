import os
from collections import Counter

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        continuous_numbers = [1 for _ in range(n)]
        for j, v in enumerate(a):
            if j == 0:
                continue
            if v > a[j-1]:
                continuous_numbers[j] = continuous_numbers[j-1]+1
        answers[i] = f"{sum(continuous_numbers)}"
    print(answers)
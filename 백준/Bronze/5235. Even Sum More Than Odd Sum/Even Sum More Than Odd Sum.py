import os
from itertools import product
from fractions import Fraction

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        odd_sum = sum([v for v in a if v % 2 == 1])
        even_sum = sum([v for v in a if v % 2 == 0])
        answer = ""
        if odd_sum > even_sum:
            answer = "ODD"
        elif odd_sum < even_sum:
            answer = "EVEN"
        else:
            answer = "TIE"
        answers[h] = f"{answer}"
    print(answers)
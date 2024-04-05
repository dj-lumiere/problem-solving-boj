import os
from itertools import permutations
from fractions import Fraction

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for a in range(t):
        n = int(input())
        numbers = [int(input()) for _ in range(n)]
        recurring_difference = [numbers[i] - numbers[i - 1] for i in range(1, n)]
        recurring_ratio = [Fraction(numbers[i], numbers[i - 1]) for i in range(1, n)]
        if all(i == recurring_difference[0] for i in recurring_difference):
            answers[a] = f"{numbers[-1] + recurring_difference[0]}"
        elif all(i == recurring_ratio[0] for i in recurring_ratio):
            answers[a] = f"{int(numbers[-1] * recurring_ratio[0])}"
    print(answers)
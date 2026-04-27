import os
from functools import reduce
from itertools import product
from math import gcd

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for h in range(t):
        a = int(input())
        possible_numbers = set()
        for i in product(range(1, 10), repeat=a):
            possible_numbers.add(reduce(lambda x, y: x * y, i))
        answer = len(possible_numbers)
        answers[h] = f"{answer}"
    print(answers)
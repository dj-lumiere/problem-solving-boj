import os
from collections import Counter
from itertools import product
from array import array
from functools import reduce

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for h in range(t):
        b = int(input())
        string = list(input())
        answer = []
        current_number = 0
        for i, v in enumerate(string):
            current_number += (1 if v == ord("I") else 0) << (7 - (i % 8))
            if (i + 1) % 8 == 0:
                answer.append(current_number)
                current_number = 0
        answers[h] = f"Case #{h + 1}: " + "".join(map(chr, answer))
    print(answers)
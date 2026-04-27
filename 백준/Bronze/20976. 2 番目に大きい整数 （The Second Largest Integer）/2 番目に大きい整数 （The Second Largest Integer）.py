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
    for h in range(t):
        numbers = [int(input()) for _ in range(3)]
        numbers.sort(key=lambda x:-x)
        answer = numbers[1]
        answers[h] = f"{answer}"
    print(answers)
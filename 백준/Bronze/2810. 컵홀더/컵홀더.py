import os
import re

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        seat = input().decode()
        possible_seats = [i for i in re.split("(S|LL)", seat) if i]
        answers[i] = f"{min(n, len(possible_seats) + 1)}"
    print(answers)
import os
from itertools import combinations

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        pass
    while True:
        sentence = input().decode().strip()
        if sentence == "#":
            break
        answers.append(" ".join(x[::-1] for x in sentence.split(" ")))
    print(answers)
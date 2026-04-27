import os
from collections import Counter
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    MOD = 10001
    answers = ["" for _ in range(t)]
    for h in range(t):
        sentence = input().decode().strip().upper()
        consonants = 0
        vowels = 0
        for v in sentence:
            if v == " ":
                continue
            if v in "AEIOU":
                vowels += 1
            else:
                consonants += 1
        answers[h] = f"{consonants} {vowels}"
    print(answers)
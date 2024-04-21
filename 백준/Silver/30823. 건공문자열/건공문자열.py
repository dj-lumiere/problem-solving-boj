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
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        k = int(input())
        s = ' ' + input().decode()
        s2 = list(range(n + 1))
        s2 = s2[k:] + (s2[1:k] if (n - k + 1) % 2 == 0 else s2[1:k][::-1])
        answer = "".join([s[i] for i in s2])
        answers[h] = f"{answer}"
    print(answers)
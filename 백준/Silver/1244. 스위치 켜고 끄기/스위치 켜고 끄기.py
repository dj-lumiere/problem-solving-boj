import os
from collections import Counter
from itertools import combinations, product
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
        switches = [0] + [int(input()) for _ in range(n)]
        q = int(input())
        for _ in range(q):
            a, b = int(input()), int(input())
            if a == 1:
                for i, v in enumerate(switches):
                    if i % b == 0 and i != 0:
                        switches[i] ^= 1
            if a == 2:
                switches[b] ^= 1
                start = b - 1
                end = b + 1
                while start >= 1 and end <= n:
                    if switches[start] == switches[end]:
                        switches[start] ^= 1
                        switches[end] ^= 1
                        start -= 1
                        end += 1
                    else:
                        break
            eprint(switches)
        answer = "\n".join(" ".join(map(str, switches[i*20+1:i*20+21])) for i in range(n//20+1))
        answers[h] = f"{answer}"
    print(answers)
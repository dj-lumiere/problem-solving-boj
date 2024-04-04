import os
import re
from collections import Counter

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    keumminsoo = [i for i in range(1000001) if all(j == "4" or j == "7" for j in str(i))]
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        for j, v in enumerate(keumminsoo):
            if v > n:
                answers[i] = str(keumminsoo[j - 1])
                break
        else:
            answers[i] = str(keumminsoo[-1])
    print(answers)
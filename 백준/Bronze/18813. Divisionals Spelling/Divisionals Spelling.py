import os
from collections import Counter
from itertools import permutations

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
        a = [input().decode() for _ in range(n)]
        answer = 0
        for v in a:
            if sorted(set(v)) == sorted(v) and all(0 <= ord(i) - ord("A") < k for i in v):
                answer += 1
        answers[h] = f"{answer}"
    print(answers)
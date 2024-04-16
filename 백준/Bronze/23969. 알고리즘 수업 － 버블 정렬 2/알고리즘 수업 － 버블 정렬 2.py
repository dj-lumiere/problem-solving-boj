import os
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
        a = [0] + [int(input()) for _ in range(n)]
        for last in range(n, 1, -1):
            for i in range(1, last):
                if a[i] > a[i + 1] and k > 0:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    k -= 1
        if k == 0:
            answer = " ".join(map(str, a[1:]))
        else:
            answer = "-1"
        answers[h] = answer
    print(answers)
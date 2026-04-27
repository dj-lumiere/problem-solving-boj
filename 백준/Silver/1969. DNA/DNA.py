import os
from collections import Counter
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 10001
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        m = int(input())
        dnas = [input().decode() for _ in range(n)]
        frequency = [Counter(dnas[i][j] for i in range(n)) for j in range(m)]
        answer1 = ""
        for v in frequency:
            most_frequent = v.most_common(n)
            most_frequent.sort(key=lambda x:(-x[1], x[0]))
            answer1 += most_frequent[0][0]
        eprint(frequency)
        answer2 = sum([sum(a!=b for a,b in zip(i, answer1)) for i in dnas])
        answers[h] = f"{answer1}\n{answer2}"
    print(answers)
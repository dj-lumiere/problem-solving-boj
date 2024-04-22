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
        m = int(input())
        chicken_satis = [[int(input()) for _ in range(m)] for _ in range(n)]
        results = []
        for i, j, k in combinations(range(m), 3):
            result_sub =sum([max(chicken_satis[a][i], chicken_satis[a][j], chicken_satis[a][k]) for a in range(n)])
            results.append(result_sub)
            eprint([i, j, k, result_sub])
        answer = max(results)
        answers[h] = f"{answer}"
    print(answers)
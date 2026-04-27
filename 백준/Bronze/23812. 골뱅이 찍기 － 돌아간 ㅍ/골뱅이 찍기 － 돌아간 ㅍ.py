import os
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    fill_cell = [(0,0),(0,4)]+[(2,0),(2,4)]+[(4,0),(4,4)]+[(1,i) for i in range(5)]+[(3,i) for i in range(5)]
    for i in range(t):
        n = int(input())
        answer = [[" " for _ in range(5*n)] for _ in range(5*n)]
        for j, k in fill_cell:
            for l, m in product(range(n), repeat=2):
                answer[j*n+l][k*n+m] = "@"
        answers[i] = "\n".join("".join(x) for x in answer)
    print(answers)
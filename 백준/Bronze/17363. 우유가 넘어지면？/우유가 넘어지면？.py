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
    rotation = {".": ".", "O": "O", "-": "|", "|": "-", "/": "\\", "\\": "/", "^": "<", "<": "v", "v": ">", ">": "^"}
    for i in range(t):
        n, m = int(input()), int(input())
        grid = [input().decode() for _ in range(n)]
        answer = [["" for _ in range(n)] for _ in range(m)]
        for r, c in product(range(n), range(m)):
            answer[-c - 1][r] = rotation[grid[r][c]]
        answers[i] = "\n".join("".join(x) for x in answer)
    print(answers)
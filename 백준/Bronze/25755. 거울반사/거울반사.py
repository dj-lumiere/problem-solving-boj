import os
from itertools import product
from fractions import Fraction

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    conversion = {f"{i}": "?" for i in range(1, 10)}
    conversion["1"] = "1"
    conversion["2"] = "5"
    conversion["5"] = "2"
    conversion["8"] = "8"
    answers = ["" for _ in range(t)]
    for h in range(t):
        w = input().decode()
        n = int(input())
        grid = [[input().decode() for _ in range(n)] for _ in range(n)]
        answer = [["" for _ in range(n)] for _ in range(n)]
        if w == "L" or w == "R":
            for i, j in product(range(n), repeat=2):
                answer[i][j] = conversion[grid[i][-j - 1]]
        if w == "U" or w == "D":
            for i, j in product(range(n), repeat=2):
                answer[i][j] = conversion[grid[-i - 1][j]]
        answers[h] = "\n".join(" ".join(x) for x in answer)
    print(answers)
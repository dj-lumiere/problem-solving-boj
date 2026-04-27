import os
from collections import Counter
from itertools import combinations, permutations, product
from array import array
from functools import reduce
from math import factorial

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    prev_answer = 1
    for h in range(t):
        n = int(input())
        grid = [[0] * (n + 2)] + [[0] + list(input().decode().strip()) + [0] for _ in range(n)] + [[0] * (n + 2)]
        answer_grid = [["" for _ in range(n)] for _ in range(n)]
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                neighbors = [grid[i + k][j + l] for k, l in delta]
                neighbor_sum = sum(int(k) if k != "." else 0 for k in neighbors)
                if grid[i][j] == ".":
                    answer_grid[i - 1][j - 1] = "M" if neighbor_sum >= 10 else str(neighbor_sum)
                else:
                    answer_grid[i - 1][j - 1] = "*"
        answer = "\n".join("".join(x) for x in answer_grid)
        answers[h] = f"{answer}"
    print(answers)
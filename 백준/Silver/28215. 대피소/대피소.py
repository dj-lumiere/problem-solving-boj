import os
from itertools import combinations

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        k = int(input())
        houses = [[int(input()), int(input())] for _ in range(n)]
        distance_max = []
        for camps in combinations(houses, k):
            distances = [min(abs(i1 - i2) + abs(j1 - j2) for i2, j2 in camps) for i1, j1 in houses]
            distance_max.append(max(distances))
        answer = min(distance_max)
        answers[h] = (f"{answer}")
    print(answers)
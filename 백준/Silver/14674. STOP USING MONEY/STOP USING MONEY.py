import os
from fractions import Fraction

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for a in range(t):
        n, k = int(input()), int(input())
        games = []
        for _ in range(n):
            i, c, h = [int(input()) for _ in range(3)]
            games.append((Fraction(h, c), c, i))
        games.sort(key=lambda x: (-x[0], x[1], x[2]))
        answer = []
        for i in range(k):
            answer.append(games[i][2])
        answers[a] = "\n".join(map(str, answer))
    print(answers)
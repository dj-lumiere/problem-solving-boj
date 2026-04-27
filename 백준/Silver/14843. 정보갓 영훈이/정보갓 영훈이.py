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
    for i in range(t):
        n = int(input())
        younghoon_score = 0.0
        for _ in range(n):
            s, a, t, m = float(input()), int(input()), int(input()), int(input())
            younghoon_score += s * (1 + 1 / a) * (1 + m / t) / 4
        p = int(input())
        compare_score = [younghoon_score] + [float(input()) for _ in range(p)]
        compare_score.sort(reverse=True)
        if (compare_score.index(younghoon_score) + 1) * 100 <= 15 * (p + 1):
            answers[i] = f'The total score of Younghoon "The God" is {younghoon_score:.2f}.'
        else:
            answers[i] = f'The total score of Younghoon is {younghoon_score:.2f}.'
    print(answers)
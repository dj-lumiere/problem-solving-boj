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
        n, k = int(input()), int(input())
        s = [int(input()) for _ in range(n)]
        d = [int(input()) - 1 for _ in range(n)]
        answer = [j for j in s]
        for j in range(k):
            answer_new = [0 for _ in range(n)]
            for a, v in enumerate(answer):
                answer_new[d[a]] = v
            answer = answer_new
        answers[i] = " ".join(map(str, answer))
    print(answers)
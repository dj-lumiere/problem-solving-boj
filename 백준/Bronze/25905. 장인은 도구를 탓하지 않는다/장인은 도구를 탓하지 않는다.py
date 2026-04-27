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
        probability = [float(input()) for _ in range(10)]
        answer = 0
        for j in permutations(probability, r=9):
            answer_sub = 10 ** 9
            for k, v in enumerate(j, start=1):
                answer_sub *= v / k
            if answer_sub > answer:
                answer = answer_sub
        answers[i] = f"{answer}"
    print(answers)
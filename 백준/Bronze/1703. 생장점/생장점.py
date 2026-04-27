import os
from functools import reduce

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    for i in range(t):
        pass
    i = 0
    while True:
        a = int(input())
        if a == 0:
            break
        answers.append("")
        numbers = [int(input()) for _ in range(2 * a)]
        answer = 1
        for j, v in enumerate(numbers):
            if j % 2 == 0:
                answer *= v
            elif j % 2 == 1:
                answer -= v
        answers[i] = f"{answer}"
        i += 1
    print(answers)
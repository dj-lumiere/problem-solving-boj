import os
from itertools import product

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
        sequence = input().decode()
        answer = [["1", "2"], ["3", "4"]]
        for i in sequence:
            if i == "H":
                answer = [answer[1], answer[0]]
            else:
                answer = [[answer[0][1], answer[0][0]], [answer[1][1], answer[1][0]]]
        answers[h] = "\n".join(" ".join(x) for x in answer)
    print(answers)
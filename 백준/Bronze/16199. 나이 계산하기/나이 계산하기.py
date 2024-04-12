import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        y1, m1, d1 = [int(input()) for _ in range(3)]
        y2, m2, d2 = [int(input()) for _ in range(3)]
        man = y2 - y1
        count = y2 - y1 + 1
        year = y2 - y1
        if (m1, d1) > (m2, d2):
            man -= 1
        answers[i] = f"{man}\n{count}\n{year}"
    print(answers)
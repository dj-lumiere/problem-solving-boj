import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        x1, x2, y1, y2 = 101, 0, 101, 0
        for _ in range(n):
            x, y = int(input()), int(input())
            x1, x2, y1, y2 = min(x1, x), max(x2, x), min(y1, y), max(y2, y)
        answer = max(x2 - x1, y2 - y1) ** 2
        answers[h] = f"{answer}"
    print(answers)
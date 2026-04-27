import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n, a, c, p = [int(next(tokens)) for _ in range(4)]
        answers[i] = f"{(n - 1) // a * c * p}"
    os.write(1, "\n".join(answers).encode())
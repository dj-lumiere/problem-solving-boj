import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = int(next(tokens))
    answers = ["" for _ in range(t)]
    for i in range(t):
        s = int(next(tokens))
        n = int(next(tokens))
        for j in range(n):
            q, p = int(next(tokens)), int(next(tokens))
            s += q*p
        answers[i] = str(s)
    os.write(1, "\n".join(answers).encode())
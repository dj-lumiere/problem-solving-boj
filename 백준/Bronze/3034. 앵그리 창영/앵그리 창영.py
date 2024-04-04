import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = int(next(tokens))
    w = int(next(tokens))
    h = int(next(tokens))
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(next(tokens))
        if n*n <= w*w+h*h:
            answers[i] = "DA"
        else:
            answers[i] = "NE"
    os.write(1, "\n".join(answers).encode())
import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(next(tokens))
        if 1 << (n.bit_length() - 1) == n:
            answers[i] = "1"
        else:
            answers[i] = "0"
    os.write(1, "\n".join(answers).encode())
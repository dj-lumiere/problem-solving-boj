import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    t = int(next(tokens))
    answers = ["" for _ in range(t)]
    for i in range(t):
        a, b = int(next(tokens)), int(next(tokens))
        answers[i] = f"Case {i + 1}: {a + b}"
    os.write(1, "\n".join(answers).encode())
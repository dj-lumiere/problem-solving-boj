import os

with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        numbers = map(int, next(tokens).decode().split(" "))
        answers[i] = f"{sum(numbers)}"
    os.write(1, "\n".join(answers).encode())
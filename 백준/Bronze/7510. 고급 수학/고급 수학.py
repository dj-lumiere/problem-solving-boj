import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        a, b, c = sorted([int(input()) for _ in range(3)])
        answers[i] = f"Scenario #{i + 1}:\n{'yes' if c ** 2 == a ** 2 + b ** 2 else 'no'}\n"
    print(answers)
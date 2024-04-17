import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    MOD = 100_000
    answers = ["" for _ in range(t)]
    for h in range(t):
        pass
    while True:
        n = int(input())
        if n == -1:
            break
        bit = [(n >> i) & 1 != 0 for i in range(32)]
        answer = sum([int(v) << i for i, v in enumerate(reversed(bit))])
        answers.append(f"{answer}")
    print(answers)
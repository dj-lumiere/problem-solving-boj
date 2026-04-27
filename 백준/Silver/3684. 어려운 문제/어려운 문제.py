import os
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 10001
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        inputs = [int(input()) for _ in range(n)]
        outputs = []
        x1 = inputs[0]
        a, b = 0, 0
        for x, y in product(range(10001), repeat=2):
            candidate = [x1]
            for i in range(n - 1):
                last = candidate[-1]
                last2 = (x * last + y) % MOD
                last3 = (x * last2 + y) % MOD
                if inputs[i + 1] != last3:
                    break
                candidate.append(last3)
            else:
                a, b = x, y
                outputs = [(a * i + b) % MOD for i in inputs]
                break
        answer = "\n".join(map(str, outputs))
        answers[h] = f"{answer}"
    print(answers)
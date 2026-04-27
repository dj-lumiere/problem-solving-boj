import os
from itertools import product

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    MOD = 10001
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = input().decode()
        n_len = len(n)
        n = "0" * ((3 - n_len % 3) % 3) + n
        n_words = [n[3 * i:3 * i + 3] for i in range(len(n) // 3)]
        answer = ",".join(n_words).strip("0")
        answers[h] = f"{answer}"
    print(answers)
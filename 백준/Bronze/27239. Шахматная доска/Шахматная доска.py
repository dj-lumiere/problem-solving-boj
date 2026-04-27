import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    INF = 10 ** 18
    for h in range(t):
        n = int(input())
        r, c = divmod(n - 1, 8)
        answers[h] = f"{chr(ord('a') + c)}{r + 1}"
    print(answers)
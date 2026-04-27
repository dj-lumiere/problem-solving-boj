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
        m = int(input())
        n_m = n - m
        k = int(input())
        n_k = n - k
        answer = min(k, m) + min(n_m, n_k)
        answers[h] = f"{answer}"
    print(answers)
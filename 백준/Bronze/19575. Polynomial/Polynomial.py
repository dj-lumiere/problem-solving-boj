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
    for i in range(t):
        n, x = [int(input()) for _ in range(2)]
        answer = 0
        for _ in range(n + 1):
            a_i, j = [int(input()) for _ in range(2)]
            answer = (x * answer + a_i) % MOD
        answers[i] = f"{answer}"
    print(answers)
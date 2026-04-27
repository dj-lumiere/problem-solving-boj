import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 0
    answers = ["" for _ in range(t)]
    for h in range(t):
        pass
    while True:
        n, m, p = [int(input()) for _ in range(3)]
        if n == m == p == 0:
            break
        x = [0] + [int(input()) for _ in range(n)]
        answer = 100 * sum(x) * (100 - p) // 100
        if x[m] == 0:
            answer = 0
        else:
            answer //= x[m]
        answers.append(f"{answer}")
    print(answers)
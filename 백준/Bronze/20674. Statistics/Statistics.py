import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        p = [int(input()) for _ in range(n)]
        answer = 0
        for i, v in enumerate(p):
            if i == 0:
                continue
            if v > p[i - 1]:
                p[i] = p[i - 1]
                answer += v - p[i - 1]
        answers[h] = f"{answer}"
    print(answers)
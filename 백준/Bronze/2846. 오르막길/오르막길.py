import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        p = [int(input()) for _ in range(n)]
        answer = [0 for _ in range(n)]
        for j, v in enumerate(p):
            if j == 0:
                answer[j] = 0
                continue
            if p[j] > p[j - 1]:
                answer[j] = answer[j - 1] + p[j] - p[j - 1]
        answers[i] = str(max(answer))
    print(answers)
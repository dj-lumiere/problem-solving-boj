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
        a = [int(input()) for _ in range(n - 1)]
        answer = [0 for _ in range(n)]
        answer[0] = 1
        for i, v in enumerate(a, start=2):
            answer[v + 1] = i
        answers[h] = " ".join(map(str, answer))
    print(answers)
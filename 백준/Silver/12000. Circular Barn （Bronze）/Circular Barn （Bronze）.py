import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for i in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        distance = [0 for _ in range(n)]
        distance2 = [[(j - k) % len(a) for j, _ in enumerate(a)] for k, _ in enumerate(a)]
        for k, v1 in enumerate(a):
            x = [v2 * distance2[k][j] for j, v2 in enumerate(a)]
            distance[k] = sum(v2 * distance2[k][j] for j, v2 in enumerate(a))
        answers[i] = str(min(distance))
    print(answers)
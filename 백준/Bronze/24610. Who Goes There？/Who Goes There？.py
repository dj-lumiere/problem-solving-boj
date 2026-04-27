import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    prev_answer = 1
    for h in range(t):
        n = int(input())
        m = int(input())
        x = [int(input()) for _ in range(m)]
        answer = [0 for _ in range(m)]
        teams = 0
        while True:
            for j, v in enumerate(x):
                if answer[j] < v:
                    answer[j] += 1
                    teams += 1
                if teams >= n:
                    break
            if teams >= n or all(i == j for i, j in zip(x, answer)):
                break
        answers[h] = "\n".join(map(str, answer))
    print(answers)
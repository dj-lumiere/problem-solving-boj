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
        a = [int(input()) for _ in range(9)]
        b = [int(input()) for _ in range(9)]
        score_difference = [0 for _ in range(18)]
        for i, (a1, b1) in enumerate(zip(a, b)):
            if i == 0:
                score_difference[i * 2] = a1
                score_difference[i * 2 + 1] = score_difference[i * 2] - b1
                continue
            score_difference[i * 2] = score_difference[i * 2 - 1] + a1
            score_difference[i * 2 + 1] = score_difference[i * 2] - b1
        answers[h] = "Yes" if score_difference[-1] < 0 and any(i > 0 for i in score_difference[:-1]) else "No"
    print(answers)
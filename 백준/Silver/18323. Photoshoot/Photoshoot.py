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
        b = [int(input()) for _ in range(n - 1)]
        answer = [[0 for _ in range(n)] for _ in range(1, n + 1)]
        for i in range(n):
            answer[i][0] = i + 1
        for j in range(n):
            for i, v in enumerate(b):
                answer[j][i + 1] = v - answer[j][i]
        answer_filter = []
        for v in answer:
            if sorted(v) == list(range(1, n + 1)):
                answer_filter.append(v)
        answer_filter.sort()
        answers[h] = " ".join(map(str, answer_filter[0]))
    print(answers)
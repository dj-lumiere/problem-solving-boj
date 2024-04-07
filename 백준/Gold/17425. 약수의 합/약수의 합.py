import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    result = [1 for _ in range(1000001)]
    for i in range(2, 1000001):
        for j in range(i, 1000001, i):
            result[j] += i
    accsum = [0 for _ in range(1000001)]
    for i in range(1, 1000001):
        accsum[i] = result[i]+accsum[i-1]
    for i in range(t):
        n = int(input())
        answers[i] = f"{accsum[n]}"
    print(answers)
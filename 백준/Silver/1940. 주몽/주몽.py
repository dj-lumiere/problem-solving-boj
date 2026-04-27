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
        m = int(input())
        a = [int(input()) for _ in range(n)]
        answer = 0
        for i1, v1 in enumerate(a):
            for i2, v2 in enumerate(a):
                if i1 >= i2:
                    continue
                if v1 + v2 == m:
                    answer += 1
        answers[h] = f"{answer}"
    print(answers)
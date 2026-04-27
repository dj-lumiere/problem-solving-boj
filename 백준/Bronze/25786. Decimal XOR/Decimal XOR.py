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
        n = list(map(int, input().decode()))
        m = list(map(int, input().decode()))
        if len(n) > len(m):
            m = [0] * (len(n) - len(m)) + m
        elif len(n) < len(m):
            n = [0] * (len(m) - len(n)) + n
        answer = [0] * len(n)
        for j, (v1, v2) in enumerate(zip(n, m)):
            answer[j] = 0 if (v1 <= 2 and v2 <= 2) or (v1 >= 7 and v2 >= 7) else 9
        answers[i] = "".join(map(str, answer))
    print(answers)
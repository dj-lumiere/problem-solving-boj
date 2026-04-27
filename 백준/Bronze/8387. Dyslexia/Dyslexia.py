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
        a = input().decode()
        b = input().decode()
        answer = sum(j == k for j, k in zip(a, b))
        answers[i] = f"{answer}"
    print(answers)
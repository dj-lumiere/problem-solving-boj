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
        penguin_position = a.index(-1)
        answers[i] = f"{min(a[:penguin_position])+min(a[penguin_position+1:])}"
    print(answers)
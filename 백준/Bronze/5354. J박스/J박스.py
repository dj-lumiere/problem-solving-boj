import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    MOD = 10 ** 9 + 7
    for a in range(t):
        n = int(input())
        grid = [["J" if 1 <= i < n - 1 and 1 <= j < n - 1 else "#" for i in range(n)] for j in range(n)]
        answer = "\n".join("".join(x) for x in grid)
        answers[a] = f"{answer}"
    print(answers)
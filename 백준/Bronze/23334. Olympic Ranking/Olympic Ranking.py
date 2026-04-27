import os

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split(b"\n"))
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = 1
    answers = ["" for _ in range(t)]
    for h in range(t):
        n = int(input())
        teams = []
        for _ in range(n):
            a, b, c, *name = input().decode().split()
            teams.append((int(a), int(b), int(c), " ".join(name)))
        teams.sort(key=lambda x: (-x[0], -x[1], -x[2]))
        answer = teams[0][3]
        answers[h] = f"{answer}"
    print(answers)
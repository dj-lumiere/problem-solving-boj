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
        a = input().decode()
        b = input().decode()
        intersect = (0, 0)
        grid = [["." for _ in range(len(a))] for _ in range(len(b))]
        for i, v in enumerate(a):
            if v in b:
                intersect = (i, b.index(v))
                break
        grid[intersect[1]] = list(a)
        for i, v in enumerate(b):
            grid[i][intersect[0]] = v
        answer = "\n".join("".join(x) for x in grid)
        answers[h] = f"{answer}"
    print(answers)
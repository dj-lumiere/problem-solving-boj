from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for _ in range(t):
        code = input()
        n = int(input())
        matches = []
        for _ in range(n):
            reg_code = input()
            match = True
            for sc, rc in zip(code, reg_code):
                if sc != '*' and sc != rc:
                    match = False
                    break
            if match:
                matches.append(reg_code)
        answer = f"{len(matches)}\n" + "\n".join(matches)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
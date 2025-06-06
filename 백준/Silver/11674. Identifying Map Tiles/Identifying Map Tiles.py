from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        s = input()
        level = len(s)
        x = 0
        y = 0
        for i, char in enumerate(s):
            bit = level - i
            mask = 1 << (level - i - 1)
            digit = int(char)
            if digit & 1:
                x += mask
            if digit & 2:
                y += mask
        answer = f"{level} {x} {y}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
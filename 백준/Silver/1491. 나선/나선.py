from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        N = int(input())
        M = int(input())
        left, right, bottom, top = 0, N - 1, 0, M - 1
        x, y = left, bottom
        direction = 0
        last_x, last_y = x, y
        while left <= right and bottom <= top:
            if direction == 0:
                for x in range(left, right + 1):
                    last_x, last_y = x, y
                bottom += 1
            elif direction == 1:
                for y in range(bottom, top + 1):
                    last_x, last_y = x, y
                right -= 1
            elif direction == 2:
                for x in range(right, left - 1, -1):
                    last_x, last_y = x, y
                top -= 1
            elif direction == 3:
                for y in range(top, bottom - 1, -1):
                    last_x, last_y = x, y
                left += 1
            direction = (direction + 1) % 4
        answer = f"{last_x} {last_y}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
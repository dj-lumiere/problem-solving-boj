from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(t):
        m = int(input())
        n = int(input())
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        turns = 0
        direction = 0
        while top <= bottom and left <= right:
            if direction == 0:
                top += 1
            elif direction == 1:
                right -= 1
            elif direction == 2:
                bottom -= 1
            elif direction == 3:
                left += 1
            direction = (direction + 1) % 4
            if top <= bottom and left <= right:
                turns += 1
        answer = f"{turns}"
        answers.append(answer)
    print(*answers, sep="\n")
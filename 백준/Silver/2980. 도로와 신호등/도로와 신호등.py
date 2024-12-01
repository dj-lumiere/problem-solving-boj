from sys import stderr, stdout

with open(0, 'r') as f:
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
    for hh in range(t):
        n, l = int(input()), int(input())
        lights = [tuple(int(input()) for _ in range(3)) for _ in range(n)]
        current_time = 0
        prev = 0
        for d, r, g in lights:
            current_time += (d - prev)
            cycle = r + g
            t_cycle = current_time % cycle
            if t_cycle < r:
                current_time += (r - t_cycle)
            prev = d
        current_time += (l - prev)
        answer = current_time
        answers.append(f"{answer}")
    print(*answers, sep=" ")
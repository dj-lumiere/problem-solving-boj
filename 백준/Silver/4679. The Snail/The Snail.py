from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(1, t + 1):
        H, U, D, F = (int(input()) for _ in range(4))
        if H == 0:
            break
        day = 1
        current_height = 0
        fatigue_factor = U * (F / 100)
        current_climb = U
        while True:
            if current_climb > 0:
                current_height += current_climb
            if current_height > H:
                answers.append(f"success on day {day}")
                break
            current_height -= D
            if current_height < 0:
                answers.append(f"failure on day {day}")
                break
            current_climb -= fatigue_factor
            day += 1
    print(*answers, sep="\n")
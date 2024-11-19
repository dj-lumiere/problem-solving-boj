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
        N, K = int(input()), int(input())
        turn_off_times = []
        count = 0
        current_time = 0
        for base in [15 * 60, 3 * 60, 3 * 60] + ([18 * 60, 3 * 60, 3 * 60]) * N:
            current_time += base
            if count % 3 == 0 and count != 0:
                current_time += K
            count += 1
            day, y = divmod(current_time, 24 * 60)
            y, z = divmod(y, 60)
            if day == N:
                turn_off_times.append(f"{y:02d}:{z:02d}")
        M = len(turn_off_times)
        answer = f"{M}\n" + "\n".join(turn_off_times) if M > 0 else "0"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
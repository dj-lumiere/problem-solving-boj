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
        N = int(input())
        forbidden = []
        for _ in range(N):
            start, end = input(), input()
            start_h, start_m = int(start[:2]), int(start[2:])
            end_h, end_m = int(end[:2]), int(end[2:])
            start_time = max(600, start_h * 60 + start_m - 10)
            end_time = min(1320, end_h * 60 + end_m + 10)
            forbidden.append((start_time, end_time))
        forbidden.sort()
        merged = []
        for s, e in forbidden:
            if not merged or merged[-1][1] < s:
                merged.append([s, e])
            else:
                merged[-1][1] = max(merged[-1][1], e)
        available = []
        prev = 600
        for s, e in merged:
            if prev < s:
                available.append(s - prev)
            prev = max(prev, e)
        if prev < 1320:
            available.append(1320 - prev)
        answer = max(available) if available else 0
        answers.append(f"{answer}")
    print(*answers, sep="\n")
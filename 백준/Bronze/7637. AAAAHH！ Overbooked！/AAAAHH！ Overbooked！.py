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
    t = INF
    answers = []


    def to_minutes(time_str):
        hh, mm = map(int, time_str.split(':'))
        return hh * 60 + mm


    for case_num in range(1, t + 1):
        n = int(input())
        if n == 0:
            break
        events = []
        for _ in range(n):
            start, end = input().split('-')
            events.append((to_minutes(start), to_minutes(end)))
        events.sort()
        conflict = any(events[i][1] > events[i + 1][0] for i in range(n - 1))
        answers.append("conflict" if conflict else "no conflict")
    print(*answers, sep="\n")
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
        date_str = input()
        N = int(input()) - 1
        year, month, day = map(int, date_str.split('-'))
        for _ in range(N):
            day += 1
            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    days_in_month = 29
                else:
                    days_in_month = 28
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                days_in_month = 31
            else:
                days_in_month = 30
            if day > days_in_month:
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1
        answer = f"{year:04d}-{month:02d}-{day:02d}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
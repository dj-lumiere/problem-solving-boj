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
    for hh in range(t):
        n = int(input())
        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        if a > b or c > d:
            answer = "0"
        else:
            lower_x = a
            upper_x = b
            required_y_min = n - d
            required_y_max = n - c
            start_x = max(lower_x, n - d)
            end_x = min(upper_x, n - c)
            if start_x > end_x:
                count = 0
            else:
                count = end_x - start_x + 1
            count = max(0, count)
            answer = f"{count}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
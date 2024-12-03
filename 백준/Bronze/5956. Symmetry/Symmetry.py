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
        m = int(input())
        cows = 0
        q = [(n, m, 0)]
        while q:
            current_n, current_m, step = q.pop()
            if current_n % 2 == 1 and current_m % 2 == 1:
                cows += 4 ** step
                sub_n = current_n // 2
                sub_m = current_m // 2
                q.extend([(sub_n, sub_m, step + 1)])
        answer = f"{cows}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
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
    t = INF
    answers = []
    for hh in range(t):
        n = int(input())
        if n == 0:
            break
        heights = [int(input()) for _ in range(n)]
        total = sum(heights)
        target = total // n
        moves = sum(h - target for h in heights if h > target)
        answer = f"Set #{hh + 1}\nThe minimum number of moves is {moves}."
        answers.append(f"{answer}")
    print(*answers, sep="\n\n")
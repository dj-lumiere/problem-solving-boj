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
    for _ in range(t):
        s = list(input())
        multiplier = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        digits = {f"{i}": i for i in range(10)}
        digits["X"] = 10
        digits["?"] = -1
        s_val = [digits[i] for i in s]
        question = s.index("?")
        answer = "-1"
        for i in range(11):
            s_val[question] = i
            remainder = sum(x * y for x, y in zip(s_val, multiplier)) % 11
            if remainder == 0 and (i != 10 or question == len(s) - 1):
                answer = f"{i}" if i != 10 else "X"
        answers.append(answer)
    print(*answers, sep="\n")
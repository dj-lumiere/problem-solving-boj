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
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    t = int(input())
    answers = []
    for case in range(1, t + 1):
        A = int(input())
        B = int(input())
        count = 0
        for num in range(A, B + 1):
            str_num = str(num)
            if str_num != str_num[::-1]:
                continue
            sqrt = int(num ** 0.5)
            if sqrt * sqrt != num:
                continue
            if str(sqrt) != str(sqrt)[::-1]:
                continue
            count += 1
        answer = f"Case #{case}: {count}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
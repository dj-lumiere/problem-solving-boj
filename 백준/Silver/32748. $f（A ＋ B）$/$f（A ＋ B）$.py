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
        numbers = [int(input()) for _ in range(10)]
        f_rev = [0 for _ in range(10)]
        for i, v in enumerate(numbers):
            f_rev[v] = i
        f_a = list(map(int, input()))
        f_b = list(map(int, input()))
        a = [f_rev[i] for i in f_a]
        b = [f_rev[i] for i in f_b]
        a_b = list(map(int, str(int("".join(map(str, a))) + int("".join(map(str, b))))))
        f_a_b = [numbers[i] for i in a_b]
        answer = "".join(map(str, f_a_b))
        answers.append(f"{answer}")
    print(*answers, sep="\n")
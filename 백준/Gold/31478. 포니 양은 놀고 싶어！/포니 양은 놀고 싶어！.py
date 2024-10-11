from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        a, b, c, k, l = (int(input()) for _ in range(5))
        # a^(b^c)%7, b^c*a^-1%7.
        first_mod = 1
        if (b <= 7 and c == 1) or (b <= 2 and c == 2):
            first_mod = pow(a, pow(b, c), 7)
        else:
            first_mod = pow(a, pow(b, c, 6) + 6, 7)
        second_mod = (pow(b, c, 7) * pow(a, -1, 7)) % 7
        answer = 0
        if (k + first_mod) % 7 == l:
            answer += 1
        if (k + second_mod) % 7 == l:
            answer += 2
        answers.append(answer)
    print(*answers, sep="\n")

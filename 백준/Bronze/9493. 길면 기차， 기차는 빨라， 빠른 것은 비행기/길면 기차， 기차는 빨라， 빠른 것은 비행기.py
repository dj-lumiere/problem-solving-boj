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
    t = INF
    answers = []
    for hh in range(t):
        a, b, c = (int(input()), int(input()), int(input()))
        if a == b == c == 0:
            break
        s = (c - b) * a * 36000 // (c * b)
        if s % 10 >= 5:
            s += 10
        s //= 10
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        answer = f"{h}:{m:0>2}:{s:0>2}"
        answers.append(answer)
    print(*answers, sep="\n")
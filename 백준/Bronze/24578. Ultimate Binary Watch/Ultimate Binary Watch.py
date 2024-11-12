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
        n_str = input()
        digits = [int(c) for c in n_str]
        bits = [['*' if c=='1' else '.' for c in f"{d:0>4b}"] for d in digits]
        line1 = bits[0][0] + ' ' + bits[1][0] + '   ' + bits[2][0] + ' ' + bits[3][0]
        line2 = bits[0][1] + ' ' + bits[1][1] + '   ' + bits[2][1] + ' ' + bits[3][1]
        line3 = bits[0][2] + ' ' + bits[1][2] + '   ' + bits[2][2] + ' ' + bits[3][2]
        line4 = bits[0][3] + ' ' + bits[1][3] + '   ' + bits[2][3] + ' ' + bits[3][3]
        answer = '\n'.join([line1, line2, line3, line4])
        answers.append(f"{answer}")
    print(*answers, sep="\n")
from sys import stderr, stdout


def sides(n):
    if n == 1:
        return [0, 0, 0, 0, 0, 1, 0]
    if n == 2:
        return [0, 0, 1, 0, 2, 0, 0]
    return [0, 2 * (n - 2), 1, n - 2, 2, 0, 0]


def side_max():
    return [0, 6, 11, 15, 18, 20, 21]


def side_min():
    return [0, 1, 3, 6, 10, 15, 21]


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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        sides_sum = [0, 0, 0, 0, 0, 0, 0]
        for i in range(1, n + 1):
            for j in range(7):
                sides_sum[j] += sides(i)[j]
        answer = 0
        for j in range(7):
            answer += sides_sum[j] * (side_min()[j] + side_max()[j])
        answers.append(answer)
    print(*answers, sep="\n")
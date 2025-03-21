from sys import stderr, stdout


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    if precision == 0:
        return f"{integer_part}"
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for _ in range(t):
        r_sum = g_sum = b_sum = 0
        for _ in range(10):
            r, g, b = int(input()), int(input()), int(input())
            r_sum += r
            g_sum += g
            b_sum += b
        r_avg = precise_round(r_sum, 10, 0)
        g_avg = precise_round(g_sum, 10, 0)
        b_avg = precise_round(b_sum, 10, 0)
        answer = f"{r_avg} {g_avg} {b_avg}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
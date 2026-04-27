from sys import stderr, stdout


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        h, w, c, d = (int(input()) for _ in range(4))
        grid = [[1 for _ in range(w)] for _ in range(h)]
        nine_count_row = list(range(h))
        remaining_nines = d - h * (h - 1) // 2
        for i, v in enumerate(reversed(nine_count_row), start=1):
            max_nine_count_possible = w + 1 - h
            if remaining_nines >= max_nine_count_possible:
                nine_count_row[-i] += max_nine_count_possible
                remaining_nines -= max_nine_count_possible
            elif remaining_nines > 0:
                nine_count_row[-i] += remaining_nines
                remaining_nines = 0
            else:
                break
        if any(i > w for i in nine_count_row):
            answer = "-1"
        elif remaining_nines == 0:
            for i, v in enumerate(nine_count_row):
                grid[i][:v] = [9] * v
            answer = "\n".join(" ".join(map(str, i)) for i in grid)
        else:
            answer = "-1"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
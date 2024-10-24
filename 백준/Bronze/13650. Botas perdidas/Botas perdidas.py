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
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = INF
    answers = []
    for hh in range(1, t + 1):
        n = input()
        if n is None:
            break
        n = int(n)
        boots = {}
        for _ in range(n):
            size, foot = int(input()), input()
            if (size, foot) not in boots:
                boots[(size, foot)] = 0
            boots[(size, foot)] += 1
        pairs = 0
        for size in range(30, 61):
            left = boots.get((size, 'E'), 0)
            right = boots.get((size, 'D'), 0)
            pairs += min(left, right)
        answer = pairs
        answers.append(f"{answer}")
    print(*answers, sep="\n")
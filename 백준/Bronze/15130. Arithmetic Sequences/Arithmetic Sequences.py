from decimal import getcontext
from sys import stderr, stdout

getcontext().prec = 30


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
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        numbers = [int(input()) for _ in range(10)]
        indices = [i for i, num in enumerate(numbers) if num != 0]
        if len(indices) < 2:
            answers.append("-1")
            continue
        i1, i2 = indices[0], indices[1]
        a1, a2 = numbers[i1], numbers[i2]
        if (a2 - a1) % (i2 - i1) != 0:
            answers.append("-1")
            continue
        d = (a2 - a1) // (i2 - i1)
        constructed = [a1 + d * (i - i1) for i in range(10)]
        valid = True
        for i in range(10):
            if numbers[i] != 0 and numbers[i] != constructed[i]:
                valid = False
                break
        if valid:
            answer = ' '.join(map(str, constructed))
        else:
            answer = "-1"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
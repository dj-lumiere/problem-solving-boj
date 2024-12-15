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
    input = lambda: next(tokens, "")
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
        n, k = (int(input()) for _ in range(2))
        s = input()
        box_a = []
        box_b = []
        box_c = []
        count_a = count_b = count_c = 0
        for c in s:
            if c == 's':
                if count_a < k:
                    box_a.append(c)
                    count_a += 1
                else:
                    if count_b < k:
                        box_b.append(c)
                        count_b += 1
                    elif count_c < k:
                        box_c.append(c)
                        count_c += 1
            elif c == 'r':
                if count_b < k:
                    box_b.append(c)
                    count_b += 1
                else:
                    if count_c < k:
                        box_c.append(c)
                        count_c += 1
                    elif count_a < k:
                        box_a.append(c)
                        count_a += 1
            elif c == 'p':
                if count_c < k:
                    box_c.append(c)
                    count_c += 1
                else:
                    if count_a < k:
                        box_a.append(c)
                        count_a += 1
                    elif count_b < k:
                        box_b.append(c)
                        count_b += 1
        answer = '\n'.join([''.join(box_a), ''.join(box_b), ''.join(box_c)])
        answers.append(f"{answer}")
    print(*answers, sep="\n")
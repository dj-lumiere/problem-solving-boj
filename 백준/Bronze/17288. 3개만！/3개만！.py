from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

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
        s = input()
        count = 0
        n = len(s)
        for i in range(n - 2):
            if s[i].isdigit() and s[i + 1].isdigit() and s[i + 2].isdigit():
                a, b, c = int(s[i]), int(s[i + 1]), int(s[i + 2])
                if b == a + 1 and c == b + 1:
                    if (i == 0 or not (s[i - 1].isdigit() and int(s[i - 1]) == a - 1)) and (
                            i + 3 >= n or not (s[i + 3].isdigit() and int(s[i + 3]) == c + 1)):
                        count += 1
        answer = count
        answers.append(f"{answer}")
    print(*answers, sep="\n")
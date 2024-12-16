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
    tokens = iter(f.read().splitlines())
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
        l, h, p, e, n = map(int, input().split())
        total_r = {'Lab': 0, 'Hw': 0, 'Proj': 0, 'Exam': 0}
        total_s = {'Lab': 0, 'Hw': 0, 'Proj': 0, 'Exam': 0}
        for _ in range(n):
            line = input()
            parts = line.split()
            cat = parts[0]
            r_s = parts[2]
            r, s = map(int, r_s.split('/'))
            total_r[cat] += r
            total_s[cat] += s
        grade = Fraction(l) * Fraction(total_r['Lab'], total_s['Lab']) + Fraction(h) * Fraction(
            total_r['Hw'], total_s['Hw']) + Fraction(p) * Fraction(
            total_r['Proj'], total_s['Proj']) + Fraction(e) * Fraction(total_r['Exam'], total_s['Exam'])
        answer = grade.numerator // grade.denominator
        answers.append(f"{answer}")
    print(*answers, sep="\n")
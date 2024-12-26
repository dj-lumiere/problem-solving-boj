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
        s1 = input()
        h1, m1 = map(int, s1.split(':'))
        t1 = h1 * 60 + m1
        s2 = input()
        h2, m2 = map(int, s2.split(':'))
        t2 = h2 * 60 + m2
        s3 = input()
        h3, m3 = map(int, s3.split(':'))
        p1 = h3 * 60 + m3
        s4 = input()
        h4, m4 = map(int, s4.split(':'))
        p2 = h4 * 60 + m4
        a, b, c = p1, p2, t2 - t1
        a0, b0 = a, b
        x0, y0 = 1, 0
        x1, y1 = 0, 1
        while b != 0:
            q = a // b
            a, b = b, a % b
            x0, y0, x1, y1 = x1, y1, x0 - q * x1, y0 - q * y1
        g = a
        x = x0
        if c % g != 0:
            answer = "Never"
        else:
            lcm = p1 * p2 // g
            x = (c // g * x) % (b0 // g)
            t_time = t1 + p1 * x
            t_time %= lcm
            while t_time < max(t1, t2):
                t_time += lcm
            days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            day_index = (t_time // 1440) % 7
            day = days[day_index]
            time_h = t_time % 1440 // 60
            time_m = t_time % 60
            answer = f"{day}\n{time_h:02d}:{time_m:02d}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
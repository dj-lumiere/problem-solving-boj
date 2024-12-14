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
        n = int(input())
        tokens = [input() for _ in range(2 * n + 1)]
        morse_values = {'.': 1, '-': 5, ':': 2, '=': 10}
        values = []
        ops = []
        for i, token in enumerate(tokens):
            if i % 2 == 0:
                val = 0
                for c in token:
                    val += morse_values[c]
                values.append(val)
            else:
                ops.append(token)
        expr_values = [values[0]]
        for i in range(n):
            op = ops[i]
            next_val = values[i + 1]
            if op == '*':
                expr_values[-1] *= next_val
            elif op == '+':
                expr_values.append(next_val)
        total = sum(expr_values)
        answer = total
        answers.append(f"{answer}")
    print(*answers, sep="\n")
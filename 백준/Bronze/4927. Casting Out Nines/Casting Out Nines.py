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
    t = INF
    answers = []
    for hh in range(t):
        s = input()
        if s == '.':
            break
        a, op_b_eq_c = s.split('+') if '+' in s else s.split('*')
        op = '+' if '+' in s else '*'
        b, c = op_b_eq_c.split('=')
        a_sum = sum(map(int, a))
        b_sum = sum(map(int, b))
        c_sum = sum(map(int, c.rstrip('.')))
        if op == '+':
            result = (a_sum + b_sum) % 9
        else:
            result = (a_sum * b_sum) % 9
        c_mod = c_sum % 9
        answer = f"{hh + 1}. {'PASS' if result == c_mod else 'NOT!'}"
        answers.append(answer)
    print(*answers, sep="\n")
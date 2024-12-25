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
    answers = []
    n = int(input())
    matrices = {}
    for _ in range(n):
        name, r, c = input(), int(input()), int(input())
        matrices[name] = (r, c)
    t = INF
    for hh in range(t):
        expr = input()
        if expr is None:
            break
        stack = []
        error = False
        mult = 0
        for char in expr:
            if char == '(':
                continue
            elif char == ')':
                if len(stack) < 2:
                    error = True
                    break
                (r2, c2, m2) = stack.pop()
                (r1, c1, m1) = stack.pop()
                if c1 != r2:
                    error = True
                    break
                mult += r1 * c1 * c2
                stack.append((r1, c2, m1 + m2 + r1 * c1 * c2))
            else:
                if char not in matrices:
                    error = True
                    break
                r, c = matrices[char]
                stack.append((r, c, 0))
        if error or len(stack) != 1:
            answers.append("error")
        else:
            answers.append(str(stack[0][2]))
    print(*answers, sep="\n")
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
    t = int(input())
    answers = []
    for hh in range(t):
        type_char = input()
        mom_height = input()
        dad_height = input()
        feet, inches = mom_height.split("'")
        mom = int(feet) * 12 + int(inches.strip('"'))
        feet, inches = dad_height.split("'")
        dad = int(feet) * 12 + int(inches.strip('"'))
        if type_char == 'B':
            child = Fraction(mom + dad + 5, 2)
        else:
            child = Fraction(mom + dad - 5, 2)
        lower = child - 4
        upper = child + 4
        A = int(lower) + (1 if lower - int(lower) > 0 else 0)
        B = int(upper)
        A_feet, A_inches = divmod(A, 12)
        B_feet, B_inches = divmod(B, 12)
        answer = f"Case #{hh + 1}: {A_feet}'{A_inches}\" to {B_feet}'{B_inches}\""
        answers.append(f"{answer}")
    print(*answers, sep="\n")
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
        line = input()
        if line == 'BYE':
            break
        pos = line.find('+')
        A = line[:pos]
        pos2 = line.find('=')
        B = line[pos + 1:pos2]
        code_to_digit = {'063': '0', '010': '1', '093': '2', '079': '3', '106': '4', '103': '5', '119': '6', '011': '7', '127': '8', '107': '9'}
        digit_to_code = {v: k for k, v in code_to_digit.items()}
        a = ''.join([code_to_digit[A[i:i + 3]] for i in range(0, len(A), 3)])
        b = ''.join([code_to_digit[B[i:i + 3]] for i in range(0, len(B), 3)])
        s = int(a) + int(b)
        c = ''.join([digit_to_code[d] for d in str(s)])
        answer = f"{A}+{B}={c}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
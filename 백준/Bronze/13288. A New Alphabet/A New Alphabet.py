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
    mapping = {'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3', 'f': '#', 'g': '6', 'h': '[-]', 'i': '|', 'j': '_|', 'k': '|<', 'l': '1', 'm': '[]\\/[]', 'n': '[]\\[]', 'o': '0', 'p': '|D', 'q': '(,)', 'r': '|Z', 's': '$', 't': '\'][\'', 'u': '|_|', 'v': '\\/', 'w': '\\/\\/', 'x': '}{', 'y': '`/', 'z': '2'}
    for hh in range(t):
        s = input()
        answer = ''.join([mapping[c.lower()] if c.isalpha() else c for c in s])
        answers.append(f"{answer}")
    print(*answers, sep="\n")
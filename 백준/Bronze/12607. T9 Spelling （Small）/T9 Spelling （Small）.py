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
    t = int(input()) if True else INF
    answers = []
    mapping = {'a': '2', 'b': '22', 'c': '222', 'd': '3', 'e': '33', 'f': '333', 'g': '4', 'h': '44', 'i': '444', 'j': '5', 'k': '55', 'l': '555', 'm': '6', 'n': '66', 'o': '666', 'p': '7', 'q': '77', 'r': '777', 's': '7777', 't': '8', 'u': '88', 'v': '888', 'w': '9', 'x': '99', 'y': '999', 'z': '9999', ' ': '0'}
    for hh in range(t):
        message = input()
        result = ''
        prev = ''
        for char in message:
            seq = mapping[char]
            if prev and seq[0] == prev[-1]:
                result += ' '
            result += seq
            prev = seq
        answer = f"Case #{hh + 1}: {result}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
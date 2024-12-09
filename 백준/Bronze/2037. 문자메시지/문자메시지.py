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
    key_mapping = {
        ' ': (1, 1),
        'A': (2, 1), 'B': (2, 2), 'C': (2, 3),
        'D': (3, 1), 'E': (3, 2), 'F': (3, 3),
        'G': (4, 1), 'H': (4, 2), 'I': (4, 3),
        'J': (5, 1), 'K': (5, 2), 'L': (5, 3),
        'M': (6, 1), 'N': (6, 2), 'O': (6, 3),
        'P': (7, 1), 'Q': (7, 2), 'R': (7, 3), 'S': (7, 4),
        'T': (8, 1), 'U': (8, 2), 'V': (8, 3),
        'W': (9, 1), 'X': (9, 2), 'Y': (9, 3), 'Z': (9, 4),
    }
    for hh in range(t):
        p, w = map(int, input().split())
        message = input()
        total_time = 0
        previous_key = None
        for char in message:
            key, presses = key_mapping[char]
            if previous_key == key and not (char == ' ' and previous_key == 1):
                total_time += w
            total_time += p * presses
            previous_key = key
        answer = total_time
        answers.append(f"{answer}")
    print(*answers, sep="\n")

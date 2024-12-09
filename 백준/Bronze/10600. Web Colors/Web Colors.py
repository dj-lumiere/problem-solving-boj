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
    colors = [
        ("White", 255, 255, 255),
        ("Silver", 192, 192, 192),
        ("Gray", 128, 128, 128),
        ("Black", 0, 0, 0),
        ("Red", 255, 0, 0),
        ("Maroon", 128, 0, 0),
        ("Yellow", 255, 255, 0),
        ("Olive", 128, 128, 0),
        ("Lime", 0, 255, 0),
        ("Green", 0, 128, 0),
        ("Aqua", 0, 255, 255),
        ("Teal", 0, 128, 128),
        ("Blue", 0, 0, 255),
        ("Navy", 0, 0, 128),
        ("Fuchsia", 255, 0, 255),
        ("Purple", 128, 0, 128),
    ]
    for _ in range(t):
        r, g, b = int(input()), int(input()), int(input())
        if r == -1 and g == -1 and b == -1:
            break
        min_dist = INF
        min_color = ""
        min_idx = INF
        for idx, (name, R, G, B) in enumerate(colors):
            dist = (R - r)**2 + (G - g)**2 + (B - b)**2
            if dist < min_dist or (dist == min_dist and idx < min_idx):
                min_dist = dist
                min_color = name
                min_idx = idx
        answer = min_color
        answers.append(f"{answer}")
    print(*answers, sep="\n")

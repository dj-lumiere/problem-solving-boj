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
        N, Q = int(input()), int(input())
        allocations = []
        room_alloc = [0] * (N + 1)
        for _ in range(Q):
            cmd = input()
            if cmd == 'new':
                X, Y = int(input()), int(input())
                start = -1
                count = 0
                for i in range(1, N + 1):
                    if room_alloc[i] == 0:
                        count += 1
                        if count == Y:
                            start = i - Y + 1
                            break
                    else:
                        count = 0
                if start != -1:
                    end = start + Y - 1
                    allocations.append({'active': True, 'L': start, 'R': end, 'guests': X})
                    for i in range(start, end + 1):
                        room_alloc[i] = len(allocations)
                    answer = f"{start} {end}"
                else:
                    answer = "REJECTED"
                answers.append(f"{answer}")
            elif cmd == 'in':
                A, B = int(input()), int(input())
                allocations[A - 1]['guests'] += B
            elif cmd == 'out':
                A, B = int(input()), int(input())
                allocations[A - 1]['guests'] -= B
                if allocations[A - 1]['guests'] == 0:
                    L, R = allocations[A - 1]['L'], allocations[A - 1]['R']
                    allocations[A - 1]['active'] = False
                    for i in range(L, R + 1):
                        room_alloc[i] = 0
                    answer = f"CLEAN {L} {R}"
                    answers.append(f"{answer}")
        print(*answers, sep="\n")
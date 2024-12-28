from decimal import getcontext
from sys import stderr, stdout

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
        X, C, K = (int(input()) for _ in range(3))
        logs = [tuple(int(input()) for _ in range(3)) for _ in range(K)]
        logs.sort()
        seat_assigned = {}
        student_assigned = {}
        for T, S, N in logs:
            if S in seat_assigned:
                continue
            if N in student_assigned:
                prev_S = student_assigned[N]
                del seat_assigned[prev_S]
            seat_assigned[S] = N
            student_assigned[N] = S
        sorted_students = sorted(student_assigned.items())
        answer = "\n".join(f"{num} {seat}" for num, seat in sorted_students)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
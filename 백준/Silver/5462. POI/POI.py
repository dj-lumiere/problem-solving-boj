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
        n, T_val, P = (int(input()) for _ in range(3))
        participants = [[int(input()) for _ in range(T_val)] for _ in range(n)]
        problem_not_solved = [0] * T_val
        for j in range(T_val):
            count = 0
            for i in range(n):
                if participants[i][j] == 0:
                    count += 1
            problem_not_solved[j] = count
        scores = [0] * n
        solved_counts = [0] * n
        for i in range(n):
            for j in range(T_val):
                if participants[i][j] == 1:
                    scores[i] += problem_not_solved[j]
                    solved_counts[i] += 1
        filip_score = scores[P - 1]
        filip_solved = solved_counts[P - 1]
        rank = 1
        for i in range(n):
            if i == P - 1:
                continue
            if scores[i] > filip_score:
                rank += 1
            elif scores[i] == filip_score:
                if solved_counts[i] > filip_solved:
                    rank += 1
                elif solved_counts[i] == filip_solved and (i + 1) < P:
                    rank += 1
        answer = f"{filip_score} {rank}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
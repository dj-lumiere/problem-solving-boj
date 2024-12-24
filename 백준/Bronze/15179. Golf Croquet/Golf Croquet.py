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
    for hh in range(t):
        team1 = input()
        team2 = input()
        S = int(input())
        shots = input()
        team1_score = 0
        team2_score = 0
        for i in range(S):
            shot = shots[i]
            shooter = i % 4
            if shooter == 0 or shooter == 2:
                team = 'team1'
            else:
                team = 'team2'
            if shot == 'S':
                continue
            elif shot == 'H':
                if team == 'team1':
                    team1_score += 1
                else:
                    team2_score += 1
            elif shot == 'D':
                if (team == 'team1' and team1_score == 6) or (team == 'team2' and team2_score == 6):
                    if team == 'team1':
                        team1_score += 1
                    else:
                        team2_score += 1
                else:
                    if team == 'team1':
                        team1_score += 2
                    else:
                        team2_score += 2
            elif shot == 'O':
                if team == 'team1':
                    team2_score += 1
                else:
                    team1_score += 1
            if team1_score >= 7 or team2_score >= 7:
                break
        if team1_score >= 7 or team2_score >= 7:
            if team1_score > team2_score:
                status = f"{team1} has won."
            else:
                status = f"{team2} has won."
        else:
            if team1_score > team2_score:
                status = f"{team1} is winning."
            elif team2_score > team1_score:
                status = f"{team2} is winning."
            else:
                status = "All square."
        answer = f"{team1} {team1_score} {team2} {team2_score}. {status}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
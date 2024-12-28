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
        N = int(input())
        participants = []
        for _ in range(N):
            s = input()
            s = s.strip().strip('[]{},').replace('"', '')
            fields = s.split(',')
            name = fields[0].split(':')[1]
            score = int(fields[1].split(':')[1])
            isHidden = int(fields[2].split(':')[1])
            participants.append({'name': name, 'score': score, 'isHidden': isHidden})
        sorted_participants = sorted(participants, key=lambda x: (-x['score'], x['name']))
        rank = 1
        prev_score = -1
        for i in range(len(sorted_participants)):
            if sorted_participants[i]['score'] != prev_score:
                rank = i + 1
                prev_score = sorted_participants[i]['score']
            sorted_participants[i]['rank'] = rank
        visible = [p for p in sorted_participants if p['isHidden'] == 0]
        output = sorted(visible, key=lambda x: (x['rank'], x['name']))
        answer = '\n'.join([f"{p['rank']} {p['name']} {p['score']}" for p in output])
        answers.append(f"{answer}")
    print(*answers, sep="\n")
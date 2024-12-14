from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30

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
    for _ in range(t):
        n, m = int(input()), int(input())
        team_to_members = {}
        member_to_team = {}
        for _ in range(n):
            team = input()
            cnt = int(input())
            members = [input() for _ in range(cnt)]
            team_to_members[team] = sorted(members)
            for member in members:
                member_to_team[member] = team
        for _ in range(m):
            q_name = input()
            q_type = int(input())
            if q_type == 0:
                answer = '\n'.join(team_to_members[q_name])
            else:
                answer = member_to_team[q_name]
            answers.append(f"{answer}")
    print(*answers, sep="\n")
from decimal import Decimal
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        N = int(input())
        H = int(input())
        W = int(input())
        home = H
        work = W
        for _ in range(N):
            trip1 = input()
            trip2 = input()
            trip_answers = []
            if trip1 == 'Y':
                if home > 0:
                    home -= 1
                    work += 1
                    trip_answers.append('Y')
                else:
                    trip_answers.append('N')
            else:
                if work == 0 and home > 0:
                    home -= 1
                    work += 1
                    trip_answers.append('Y')
                else:
                    trip_answers.append('N')
            if trip2 == 'Y':
                if work > 0:
                    work -= 1
                    home += 1
                    trip_answers.append('Y')
                else:
                    trip_answers.append('N')
            else:
                if home == 0 and work > 0:
                    work -= 1
                    home += 1
                    trip_answers.append('Y')
                else:
                    trip_answers.append('N')
            answer = ' '.join(trip_answers)
            answers.append(f"{answer}")
    print(*answers, sep="\n")
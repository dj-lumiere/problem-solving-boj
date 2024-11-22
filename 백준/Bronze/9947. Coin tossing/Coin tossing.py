from decimal import Decimal
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = INF
    answers = []
    for hh in range(t):
        line1 = input()
        if line1 == '# #':
            break
        name1, name2 = line1.split()
        n = int(input())
        score1 = 0
        score2 = 0
        for _ in range(n):
            call, result = input().split()
            if call == result:
                score1 +=1
            else:
                score2 +=1
        answer = f"{name1} {score1} {name2} {score2}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
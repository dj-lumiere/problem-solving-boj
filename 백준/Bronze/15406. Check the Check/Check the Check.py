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
    t = 1
    answers = []
    for hh in range(t):
        dishes = []
        while True:
            dk = input()
            if dk == "TOTAL":
                break
            pk, ck = map(int, input().split())
            dishes.append((pk, ck))
        T = int(input())
        actual_total = sum(pk * ck for pk, ck in dishes)
        if actual_total >= T:
            answer = "PAY"
        else:
            answer = "PROTEST"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
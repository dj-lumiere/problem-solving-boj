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
        n = int(input())
        call_records = {}
        for _ in range(n):
            time_str, name = input(), input()
            hours, minutes = map(int, time_str.split(':'))
            total_minutes = hours * 60 + minutes
            if name in call_records:
                call_records[name] += total_minutes
            else:
                call_records[name] = total_minutes
        fee_list = []
        for name, total in call_records.items():
            if total <= 100:
                fee = 10
            else:
                excess = total - 100
                units = (excess + 49) // 50
                fee = 10 + units * 3
            fee_list.append((-fee, name, fee))
        fee_list.sort()
        for item in fee_list:
            answer = f"{item[1]} {item[2]}"
            answers.append(f"{answer}")
    print(*answers, sep="\n")
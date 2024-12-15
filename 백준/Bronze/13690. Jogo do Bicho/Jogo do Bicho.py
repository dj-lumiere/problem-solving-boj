from decimal import Decimal, getcontext
from sys import stderr, stdout

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
    t = INF
    group_map = {}
    for i in range(25):
        for num in range(i * 4 + 1, i * 4 + 5):
            key = num if num <= 99 else 0
            group_map[key] = i + 1
    answers = []
    for hh in range(t):
        V, N, M = Decimal(input()), int(input()), int(input())
        if V == 0 and N == 0 and M == 0:
            break
        prize = Decimal('0.00')
        N_str_padded = f"{N:04}"
        M_str_padded = f"{M:04}"
        if N_str_padded[-4:] == M_str_padded[-4:]:
            prize = V * Decimal('3000')
        elif N_str_padded[-3:] == M_str_padded[-3:]:
            prize = V * Decimal('500')
        elif N_str_padded[-2:] == M_str_padded[-2:]:
            prize = V * Decimal('50')
        else:
            N_last2 = int(N_str_padded[-2:])
            M_last2 = int(M_str_padded[-2:])
            group_N = group_map.get(N_last2, -1)
            group_M = group_map.get(M_last2, -1)
            if group_N == group_M and group_N != -1:
                prize = V * Decimal('16')
        answer = f"{prize}"
        answers.append(answer)
    print(*answers, sep="\n")
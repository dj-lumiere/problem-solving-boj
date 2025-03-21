from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
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
    for _ in range(t):
        N = int(input())
        prices = [int(input()) for _ in range(N)]
        P_max = max(prices)
        P_min = min(prices)
        reimbursement_limit = P_max // 2
        reimbursement = reimbursement_limit if P_min >= reimbursement_limit else P_min
        answer = P_min - reimbursement
        answers.append(f"{answer}")
    print(*answers, sep="\n")
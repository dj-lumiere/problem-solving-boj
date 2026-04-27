from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 998_244_353
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        a, b, m = int(input()), int(input()), int(input())
        answer = 0
        if a == b == 0:
            # C<=0 or D != 0에서 실수가 아님: 즉 C>0 and D==0
            answer = m
        elif a == 1 and b == 0:
            # 모든 순서쌍이 전부 가능. 1^x=1.
            answer = (2 * m + 1) ** 2
        elif a ** 2 + b ** 2 == 1:
            # D는 아무거나, C는 2의 배수
            answer = (2 * m + 1) * (2 * (m // 2) + 1)
        elif b == 0:
            # D==0이면 C가 전부 가능
            answer = 2 * m + 1
        elif a == 0:
            # D==0이면 C가 2의 배수여야함.
            answer = 2 * (m // 2) + 1
        elif abs(a) == abs(b):
            # D가 0일 때 C가 4의 배수.
            answer = 2 * (m // 4) + 1
        else:
            # C=0 and D=0
            answer = 1
        answer %= MOD
        answers.append(answer)
    print(*answers, sep="\n")
from sys import stderr, stdout

with open(0, "r") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    x = int(input())
    answers = []
    for hh in range(1, x + 1):
        n, m = int(input()), int(input())
        sejun_army = sorted((int(input()) for _ in range(n)), reverse=True)
        sebi_army = sorted((int(input()) for _ in range(m)), reverse=True)
        while sejun_army and sebi_army:
            current_weakest_sejun, current_weakest_sebi = sejun_army.pop(), sebi_army.pop()
            if current_weakest_sejun > current_weakest_sebi:
                sejun_army.append(current_weakest_sejun)
            elif current_weakest_sebi > current_weakest_sejun:
                sebi_army.append(current_weakest_sebi)
            else:
                sejun_army.append(current_weakest_sejun)
        if not sejun_army and not sebi_army:
            answer = "C"
        elif not sejun_army:
            answer = "B"
        else:
            answer = "S"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
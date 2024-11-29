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
    t = INF
    answers = []
    for hh in range(t):
        num = input()
        if num == '#':
            break
        sum_products = 0
        for i, ch in enumerate(reversed(num)):
            sum_products += int(ch) * (2 + i)
        remainder = sum_products % 11
        check_digit = 11 - remainder
        if 1 <= check_digit <= 9:
            answer = f"{num} -> {check_digit}"
        elif check_digit == 11:
            answer = f"{num} -> 0"
        else:
            answer = f"{num} -> Rejected"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
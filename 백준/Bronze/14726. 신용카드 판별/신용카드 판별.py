from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    t = int(input())
    answers = []
    for hh in range(t):
        card = input()
        total = 0
        for i in range(16):
            digit = int(card[15 - i])
            if (i + 1) % 2 == 0:
                digit *= 2
                if digit >= 10:
                    digit -= 9
            total += digit
        answer = 'T' if total % 10 == 0 else 'F'
        answers.append(f"{answer}")
    print(*answers, sep="\n")
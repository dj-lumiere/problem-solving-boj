from itertools import product
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
        a, b, c, d = (int(input()) for _ in range(4))
        possible_numbers = list(map(lambda x: int(min("".join(map(str, x)),"".join(map(str, x[1:]+x[:1])),"".join(map(str, x[2:]+x[:2])),"".join(map(str, x[3:]+x[:3])))), product(range(1, 10), repeat=4)))
        possible_numbers = sorted(set(possible_numbers))
        answer = INF
        if int(f"{a}{b}{c}{d}") in possible_numbers:
            answer = possible_numbers.index(int(f"{a}{b}{c}{d}"))+1
        elif int(f"{b}{c}{d}{a}") in possible_numbers:
            answer = possible_numbers.index(int(f"{b}{c}{d}{a}"))+1
        elif int(f"{c}{d}{a}{b}") in possible_numbers:
            answer = possible_numbers.index(int(f"{c}{d}{a}{b}"))+1
        elif int(f"{d}{a}{b}{c}") in possible_numbers:
            answer = possible_numbers.index(int(f"{d}{a}{b}{c}"))+1
        answers.append(answer)
    print(*answers, sep="\n")
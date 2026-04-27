from sys import stderr, stdout


def sol(p, q, r):
    result = 0
    # a == 1 and b == 1 -> c == 1.  
    result += 1
    # a == 1 -> b == c
    result += min(q - 1, r - 1)
    # b == 1 -> c = 1, free a.
    result += p - 1
    # otherwise, case by case.
    # a == 2 -> b**c <= 24
    case_2 = [(4, 2), (3, 2), (2, 2), (2, 3), (2, 4)] + [(i, 1) for i in range(2, 25)]
    for a in range(2, 3):
        for b, c in case_2:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a == 3 -> b**c <= 15
    case_3 = [(3, 2), (2, 2), (2, 3)] + [(i, 1) for i in range(2, 16)]
    for a in range(3, 4):
        for b, c in case_3:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a == 4 -> b**c <= 12
    case_4 = [(3, 2), (2, 2), (2, 3)] + [(i, 1) for i in range(2, 13)]
    for a in range(4, 5):
        for b, c in case_4:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a == 5 -> b**c <= 10
    case_5 = [(3, 2), (2, 2), (2, 3)] + [(i, 1) for i in range(2, 11)]
    for a in range(5, 6):
        for b, c in case_5:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a == 6 -> b**c <= 9
    case_6 = [(3, 2), (2, 2), (2, 3)] + [(i, 1) for i in range(2, 10)]
    for a in range(6, 7):
        for b, c in case_6:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a in 7..8 -> b**c <= 8
    case_8 = [(2, 2), (2, 3)] + [(i, 1) for i in range(2, 9)]
    for a in range(7, 9):
        for b, c in case_8:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a in 9..10 -> b**c <= 7
    case_10 = [(2, 2)] + [(i, 1) for i in range(2, 8)]
    for a in range(9, 10):
        for b, c in case_10:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a in 11..16 -> b**c <= 6
    case_16 = [(2, 2)] + [(i, 1) for i in range(2, 7)]
    for a in range(11, 16):
        for b, c in case_16:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a in 17..27 -> b**c <= 5
    case_27 = [(2, 2)] + [(i, 1) for i in range(2, 6)]
    for a in range(17, 28):
        for b, c in case_27:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a in 28..64 -> b**c <= 4
    case_64 = [(2, 2)] + [(i, 1) for i in range(2, 5)]
    for a in range(28, 65):
        for b, c in case_64:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a in 65..256 -> b**c <= 3
    case_256 = [(i, 1) for i in range(2, 4)]
    for a in range(65, 256):
        for b, c in case_256:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    # a in 257..4096 -> b**c <= 2
    case_4096 = [(i, 1) for i in range(2, 3)]
    for a in range(257, 4096):
        for b, c in case_4096:
            if a ** (b ** c) == a ^ b ^ c:
                result += 1
    return result


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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    answers = []
    for hh in range(t):
        p, q, r = int(input()), int(input()), int(input())
        answer = sol(p, q, r) % MOD
        answers.append(f"{answer}")
    print(*answers, sep="\n")
from sys import stdout, stderr

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
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        permutation_order_digit = []
        possible_number = list(range(1, n + 1))
        for v in a:
            permutation_order_digit.append(possible_number.index(v))
            possible_number.pop(possible_number.index(v))
        permutation_order_digit[-1] += 1
        for i, v in enumerate(reversed(permutation_order_digit), start=1):
            if v >= i and i < n:
                permutation_order_digit[-i] -= i
                permutation_order_digit[-(i + 1)] += 1
        if permutation_order_digit[0] == n:
            answer = "-1"
        else:
            next_permutation = []
            possible_number = list(range(1, n + 1))
            for v in permutation_order_digit:
                next_permutation.append(possible_number.pop(v))
            answer = " ".join(map(str, next_permutation))
        answers.append(f"{answer}")
    print(*answers, sep="\n")

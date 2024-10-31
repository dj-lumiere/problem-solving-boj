from fractions import Fraction
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    answers = []
    for hh in range(t):
        n = int(input())
        left, right = 1, int((2*n/3)**0.5) + 2
        while left < right:
            mid = (left + right) // 2
            total = 3 * mid * (mid + 1) // 2
            if total < n:
                left = mid + 1
            else:
                right = mid
        k = left
        total_before = 3 * (k - 1) * k // 2
        pos = n - total_before
        if pos <= k:
            phrase = f"{k} dolphin" if k == 1 else f"{k} dolphins"
        elif pos <= 2 * k:
            phrase = f"{k} jump" if k == 1 else f"{k} jumps"
        else:
            phrase = "splash"
        answer = phrase
        answers.append(f"{answer}")
    print(*answers, sep="\n")
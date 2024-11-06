from math import gcd
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    answers = []
    t = 1
    for hh in range(t):
        n = int(input())
        lines = [(int(input()), int(input()), int(input())) for _ in range(n)]
        # 기울기를 correction해서 a쪽이 무조건 양수가 되게, 그리고 만약 상수가 안 좋다면 분수형태로 바꾸기.
        # 만약 둘 중 하나가 0이 된다면 다른 한 쪽은 1로 만들기. (축에 수직인 직선)
        # offset은 무조건 분모가 양수가 되게 만들기
        line_corrected = []
        answer = 0
        for a, b, c in lines:
            slope = [a, b]
            offset = [c, 1]
            if a == 0:
                offset = [c, b]
                slope = [0, 1]
            elif b == 0:
                offset = [c, a]
                slope = [1, 0]
            elif a < 0:
                slope = [-a, -b]
                offset = [-c, 1]
            g = gcd(*slope)
            x, y = slope
            slope = [x // g, y // g]
            x, y = offset
            offset = [x, g * y]
            g2 = gcd(*offset)
            x, y = offset
            offset = [x // g2, y // g2]
            a, b = slope
            c, d = offset
            line_corrected.append((((a + 0xffffffff if a < 0 else a) << 32) + (b + 0xffffffff if b < 0 else b),
                                   ((c + 0xffffffff if c < 0 else c) << 32) + (d + 0xffffffff if d < 0 else d)))
        slope_info = {}
        full_line_info = {}
        for (a, b) in line_corrected:
            if a not in slope_info:
                slope_info[a] = 0
            if a not in full_line_info:
                full_line_info[a] = {}
            if b not in full_line_info[a]:
                full_line_info[a][b] = 0
            slope_info[a] += 1
            full_line_info[a][b] += 1
        for a, v in full_line_info.items():
            for b, v2 in v.items():
                answer += n - slope_info[a]
        answer //= 2
        answers.append(f"{answer}")
    print(*answers, sep="\n")

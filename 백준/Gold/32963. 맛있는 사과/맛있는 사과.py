from bisect import bisect_right
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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        q = int(input())
        ti = [int(input()) for _ in range(n)]
        si = [int(input()) for _ in range(n)]
        tsi = [(ti[i], si[i]) for i in range(n)]
        tsi.sort(key=lambda x: x[0])
        ti_sorted = [tsi[i][0] for i in range(n)]
        # eprint(tsi)
        constant = 1 << n.bit_length()
        segtree = [[0, 0] for _ in range(2 ** (n.bit_length() + 1))]
        for i in range(constant, constant + n):
            segtree[i][0] = tsi[i - constant][1]
            segtree[i][1] = 1
        for i in range(constant - 1, 0, -1):
            segtree[i][0] = max(segtree[i * 2][0], segtree[i * 2 + 1][0])
            if segtree[i][0] == segtree[i * 2][0] == segtree[i * 2 + 1][0]:
                segtree[i][1] = segtree[i * 2][1] + segtree[i * 2 + 1][1]
            elif segtree[i][0] == segtree[i * 2][0]:
                segtree[i][1] = segtree[i * 2][1]
            else:
                segtree[i][1] = segtree[i * 2 + 1][1]
        # eprint(segtree)
        for _ in range(q):
            qi = int(input())
            idx = bisect_right(ti_sorted, qi-1)
            # eprint(qi, idx)
            left = idx + constant
            right = n - 1 + constant
            # eprint(left, right)
            result = [0, 0]
            while left <= right:
                # eprint(left, right)
                if left & 1 == 1:
                    temp_max = max(result[0], segtree[left][0])
                    if temp_max == result[0] == segtree[left][0]:
                        result[1] = result[1] + segtree[left][1]
                    elif temp_max == segtree[left][0]:
                        result[0] = segtree[left][0]
                        result[1] = segtree[left][1]
                    # eprint(left, result)
                    left += 1
                if right & 1 != 1:
                    temp_max = max(result[0], segtree[right][0])
                    if temp_max == result[0] == segtree[right][0]:
                        result[1] = result[1] + segtree[right][1]
                    elif temp_max == segtree[right][0]:
                        result[0] = segtree[right][0]
                        result[1] = segtree[right][1]
                    # eprint(right, result)
                    right -= 1
                left >>= 1
                right >>= 1
            answers.append(result[1])
    print(*answers, sep="\n")
from decimal import getcontext
from sys import stdout, stderr

getcontext().prec = 1000


class MapIndex:
    def __init__(self, function, iterable):
        self.function = function
        self.iterable = iterable

    def __len__(self):
        return len(self.iterable)

    def __getitem__(self, key):
        return self.function(self.iterable[key])


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        q = int(input())
        a = [int(input()) for _ in range(n)]
        counts = [0 for _ in range(10001)]
        for i, v in enumerate(a):
            counts[v] += 1
        for _ in range(q):
            q2 = int(input())
            if q2 == 1:
                answer = 0
                x = int(input())
                for i in range(1, 10001):
                    j, m = divmod(x, i)
                    if m:
                        continue
                    if i != j and j <= 10000 and counts[i] != 0 and counts[j] != 0:
                        answer = 1
                        break
                    if i == j and counts[i] >= 2:
                        answer = 1
                        break
                if x == 0 and counts[0] >= 2:
                    answer = 1
                answers.append(f"{answer}")
            elif q2 == 2:
                i = int(input()) - 1
                counts[a[i]] -= 1
                counts[0] += 1
                a[i] = 0
    print(*answers, sep="\n")

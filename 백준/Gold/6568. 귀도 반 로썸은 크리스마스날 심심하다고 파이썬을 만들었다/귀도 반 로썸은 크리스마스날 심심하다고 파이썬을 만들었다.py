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
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(t):
        commands = [input() for _ in range(32)]
        if any(i is None for i in commands):
            break
        commands = [int(i, base=2) for i in commands]
        pc = 0
        a = 0
        while True:
            v = commands[pc]
            pc += 1
            pc %= 32
            if v >> 5 == 0:
                commands[v & 31] = a
            elif v >> 5 == 1:
                a = commands[v & 31]
            elif v >> 5 == 2:
                if a == 0:
                    pc = v & 31
            elif v >> 5 == 3:
                continue
            elif v >> 5 == 4:
                a -= 1
                a %= 256
            elif v >> 5 == 5:
                a += 1
                a %= 256
            elif v >> 5 == 6:
                pc = v & 31
            elif v >> 5 == 7:
                break
        answer = f"{bin(a)[2:]:0>8}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")

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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        m = int(input())
        registers = [[] for _ in range(101)]
        for i in range(1, n + 1):
            shapes = input()
            registers[i].append(shapes)
        for _ in range(m):
            q, i, j = (int(input()) for _ in range(3))
            if q == 1:
                k = int(input())
                if not registers[i]:
                    registers[j] = []
                    registers[k] = []
                    continue
                register_j = registers[i][:]
                register_k = registers[i][:]
                for x, v in enumerate(register_j):
                    register_j[x] = "----" + v[4:]
                for x, v in enumerate(register_k):
                    register_k[x] = v[:4] + "----"
                registers[j] = [v for v in register_j if v != "--------"]
                registers[k] = [v for v in register_k if v != "--------"]
            if q == 2:
                k = int(input())
                if not registers[i]:
                    registers[j] = []
                    continue
                register_i = registers[i][:]
                if k == 1:
                    for x, v in enumerate(register_i):
                        register_i[x] = register_i[x][6:] + register_i[x][:6]
                if k == 2:
                    for x, v in enumerate(register_i):
                        register_i[x] = register_i[x][4:] + register_i[x][:4]
                if k == 3:
                    for x, v in enumerate(register_i):
                        register_i[x] = register_i[x][2:] + register_i[x][:2]
                registers[j] = register_i[:]
            if q == 3:
                k = int(input())
                if not registers[i] or not registers[j]:
                    registers[k] = []
                    continue
                register_i = registers[i][:]
                register_j = registers[j][:]
                last_layer = len(register_i)
                for l in reversed(range(last_layer)):
                    failed = False
                    for v1, v2 in zip(register_i[l:], register_j):
                        if any(w1 != "-" and w2 != "-" for w1, w2 in zip(v1, v2)):
                            failed = True
                            break
                    if failed:
                        last_layer = l + 1
                        break
                else:
                    last_layer = 0
                register_k = register_i[:]
                register_k.extend(["--------"] * len(register_j))
                for l, m in zip(range(last_layer, 4), range(len(register_j))):
                    layer = list(register_k[l])
                    for y, v in enumerate(register_j[m]):
                        if v == "-":
                            continue
                        layer[y] = v
                    register_k[l] = "".join(layer)
                registers[k] = [v for v in register_k if v != "--------"][:4]
            if q == 4:
                k = input()
                if not registers[i]:
                    registers[j] = []
                    continue
                register_i = registers[i][:]
                for x, v in enumerate(register_i):
                    layer = list(v)
                    for y in range(1, 8, 2):
                        if layer[y - 1] == "-":
                            continue
                        layer[y] = k
                    register_i[x] = "".join(layer)
                registers[j] = register_i[:]
        answer = ":".join(registers[100]) if registers[100] else None
        answers.append(answer)
    print(*answers, sep="\n")
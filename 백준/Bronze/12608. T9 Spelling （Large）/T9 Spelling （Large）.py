from sys import stderr, stdout

with open(0, "r") as f:
    tokens = iter(f.read().split("\n"))
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    x = int(input())
    answers = []
    key_map = {'a':'2', 'b':'22', 'c':'222', 'd':'3', 'e':'33', 'f':'333', 'g':'4', 'h':'44', 'i':'444',
               'j':'5', 'k':'55', 'l':'555', 'm':'6', 'n':'66', 'o':'666', 'p':'7', 'q':'77', 'r':'777', 's':'7777',
               't':'8', 'u':'88', 'v':'888', 'w':'9', 'x':'99', 'y':'999', 'z':'9999', ' ':'0'}
    for hh in range(1, x + 1):
        message = input()
        last = ''
        answer = []
        for c in message:
            if last and key_map[c][0] == last:
                answer.append(' ')
            answer.append(key_map[c])
            last = key_map[c][0]
        answers.append(f"Case #{hh}: {''.join(answer)}")
    print(*answers, sep="\n")
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
    t = INF
    answers = []
    for hh in range(t):
        flight_num, booked = input(), int(input())
        if flight_num == "#":
            break
        while True:
            op, num = input(), int(input())
            if op == 'X' and num == 0:
                break
            if op == 'B':
                if booked + num <=68:
                    booked +=num
            elif op == 'C':
                if num <= booked:
                    booked -=num
        if flight_num == '#':
            break
        answer = f"{flight_num} {booked}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
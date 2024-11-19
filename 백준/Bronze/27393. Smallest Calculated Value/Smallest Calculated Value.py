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
    t = 1
    answers = []
    for hh in range(t):
        a, b, c = (int(input()) for _ in range(3))
        operators = ['+', '-', '*', '/']
        min_value = INF
        for op1 in operators:
            for op2 in operators:
                if op1 == '+':
                    first = a + b
                elif op1 == '-':
                    first = a - b
                elif op1 == '*':
                    first = a * b
                elif op1 == '/':
                    if b == 0 or a % b != 0:
                        continue
                    first = a // b
                if op2 == '+':
                    result = first + c
                elif op2 == '-':
                    result = first - c
                elif op2 == '*':
                    result = first * c
                elif op2 == '/':
                    if c == 0 or first % c != 0:
                        continue
                    result = first // c
                if 0 <= result < min_value:
                    min_value = result
        answer = min_value if min_value != INF else 0
        answers.append(f"{answer}")
    print(*answers, sep="\n")
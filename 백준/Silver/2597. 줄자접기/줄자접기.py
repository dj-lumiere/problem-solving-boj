from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
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
        n = int(input())
        red1 = int(input())
        red2 = int(input())
        blue1 = int(input())
        blue2 = int(input())
        yellow1 = int(input())
        yellow2 = int(input())
        folds = [('red', red1, red2), ('blue', blue1, blue2), ('yellow', yellow1, yellow2)]
        current_length = n
        positions = {'red': sorted([red1, red2]), 'blue': sorted([blue1, blue2]), 'yellow': sorted([yellow1, yellow2])}
        for color, p1, p2 in folds:
            if positions[color][0] == positions[color][1]:
                continue
            fold_point = (positions[color][0] + positions[color][1]) / 2
            left = fold_point
            right = current_length - fold_point
            current_length = max(left, right)
            for key in positions:
                new_positions = []
                for pos in positions[key]:
                    if pos < fold_point:
                        new_positions.append(fold_point - pos)
                    else:
                        new_positions.append(pos - fold_point)
                positions[key] = sorted(new_positions)
        final_length = "0.0" if current_length == int(current_length) else f"{current_length:.1f}"
        if current_length == int(current_length):
            final_length = f"{int(current_length)}.0"
        else:
            final_length = f"{current_length:.1f}"
        answer = f"{final_length}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
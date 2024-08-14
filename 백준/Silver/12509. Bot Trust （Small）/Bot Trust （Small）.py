from sys import stdout, stderr


def sign(n):
    if n == 0:
        return 0
    return n // abs(n)


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(t):
        n = int(input())
        commands = [(input(), int(input())) for _ in range(n)]
        button_sequence = {"O": [], "B": []}
        for i, v in commands:
            button_sequence[i].append(v)
        for k, v in button_sequence.items():
            button_sequence[k] = v[::-1]
        commands.reverse()
        position = {"O": 1, "B": 1}
        time = 0
        while commands:
            color, button_position = commands[-1]
            if button_position == position[color]:
                time += 1
                button_sequence[color].pop()
                commands.pop()
                other_color = "B" if color == "O" else "O"
                if button_sequence[other_color] and position[other_color] != button_sequence[other_color][-1]:
                    position[other_color] += sign(button_sequence[other_color][-1] - position[other_color])
                continue
            if button_sequence["O"] and position["O"] != button_sequence["O"][-1]:
                position["O"] += sign(button_sequence["O"][-1] - position["O"])
            if button_sequence["B"] and position["B"] != button_sequence["B"][-1]:
                position["B"] += sign(button_sequence["B"][-1] - position["B"])
            time += 1
        answer = f"Case #{hh + 1}: {time}"
        answers.append(f"{answer}")
print(*answers, sep="\n")

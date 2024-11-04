from collections import deque
from itertools import product
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = int(input())
    answers = []
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], [None, '0', None]]
    digit_pos = {}
    for i in range(4):
        for j in range(3):
            if keypad[i][j]:
                digit_pos[keypad[i][j]] = (i, j)
            possible = set()
    queue = deque(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    possible = possible.union([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    while queue:
        current = queue.popleft()
        last_digit = current[-1]
        x, y = digit_pos[last_digit]
        for dx, dy in [(i, j) for i, j in product(range(5), range(4))]:
            nx, ny = x + dx, y + dy
            if is_inbound(nx, 4, ny, 3) and keypad[nx][ny]:
                next_digit = keypad[nx][ny]
                new_number = current + next_digit
                num = int(new_number)
                if num <= 1000 and num not in possible:
                    possible.add(num)
                    queue.append(new_number)
    eprint(possible)
    for _ in range(t):
        k = input()
        closest = min(possible, key=lambda x: (abs(x - int(k)), x))
        answer = closest
        answers.append(f"{answer}")
    print(*answers, sep="\n")
from itertools import product

DELTA = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
t = int(input())
answers = []
for hh in range(1, t + 1):
    n, m = map(int, input().split())
    a_moves = [0] + list(map(int, input().split()))
    b_moves = [0] + list(map(int, input().split()))
    aps = [[0, 0, 0, 0]] + [list(map(int, input().split())) for _ in range(m)]
    charging_area = [[[] for _ in range(11)] for _ in range(11)]
    answer = 0
    for i, (x, y, c, p) in enumerate(aps[1:], start=1):
        for x2, y2 in product(range(1, 11), repeat=2):
            if abs(x - x2) + abs(y - y2) <= c:
                charging_area[y2][x2].append(i)
    for x, y in product(range(11), repeat=2):
        if charging_area[y][x]:
            continue
        charging_area[y][x].append(0)
    a_x, a_y = 1, 1
    b_x, b_y = 10, 10
    for a_move, b_move in zip(a_moves, b_moves):
        a_dx, a_dy = DELTA[a_move]
        b_dx, b_dy = DELTA[b_move]
        a_x += a_dx
        a_y += a_dy
        b_x += b_dx
        b_y += b_dy
        sub_answer = 0
        for a, b in product(charging_area[a_y][a_x], charging_area[b_y][b_x]):
            if a == b:
                sub_answer = max(sub_answer, aps[a][3])
            else:
                sub_answer = max(sub_answer, aps[a][3]+aps[b][3])
        answer += sub_answer
    answers.append(f"#{hh} {answer}")
print(*answers, sep="\n")

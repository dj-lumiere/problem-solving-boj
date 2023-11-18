# Yellow번 - 별 가두기


def is_inbound(pos_x, x_size, pos_y, y_size):
    return 0 <= pos_x < x_size and 0 <= pos_y < y_size


N, M = map(int, input().split(" "))
grid = [list(map(int, input().split(" "))) for _ in range(N)]
DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = []
for i in range(N):
    has_cycle = True
    rotation = 0
    cur_pos_x, cur_pos_y = 0, i
    path = {(cur_pos_x, cur_pos_y, 0)}
    while True:
        dx, dy = DELTA[rotation]
        dx *= grid[cur_pos_y][cur_pos_x]
        dy *= grid[cur_pos_y][cur_pos_x]
        next_pos_x, next_pos_y = cur_pos_x + dx, cur_pos_y + dy
        if not is_inbound(next_pos_x, M, next_pos_y, N):
            has_cycle = False
            break
        cur_pos_x, cur_pos_y = next_pos_x, next_pos_y
        rotation += 1
        rotation %= 4
        if (cur_pos_x, cur_pos_y, rotation) in path:
            has_cycle = True
            answer.append(i + 1)
            break
        path.add((cur_pos_x, cur_pos_y, rotation))
answer.sort()
print(len(answer))
if answer:
    print(*answer)

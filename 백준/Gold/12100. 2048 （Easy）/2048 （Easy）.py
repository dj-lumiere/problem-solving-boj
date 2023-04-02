# 12100 2048 (Easy)
# U, D의 경우 한 행씩 밀면서 진행 (U는 0 방향으로, D는 -1 방향으로)
# L, R의 경우 한 열씩 밀면서 진행 (L은 0 방향으로, R은 -1 방향으로)
N = int(input())
tileset = [list(map(int, input().split())) for _ in range(N)]


def move_up(tileset: list[list[int]]) -> list[list[int]]:
    result = [[0 for _ in range(N)] for i in range(N)]
    for i in range(N):
        already_combined = False
        col_vec = [tileset[j][i] for j in range(N)]
        new_col_vec = []
        for j, k in enumerate(col_vec):
            if not new_col_vec and k != 0:
                new_col_vec.append(k)
            else:
                if k != 0 and new_col_vec[-1] == k and not already_combined:
                    new_col_vec[-1] += k
                    already_combined = True
                elif k != 0:
                    new_col_vec.append(k)
                    already_combined = False
        if len(new_col_vec) < N:
            new_col_vec += [0] * (N - len(new_col_vec))
        for j in range(N):
            result[j][i] = new_col_vec[j]
    return result


def move_down(tileset: list[list[int]]) -> list[list[int]]:
    result = [[0 for _ in range(N)] for i in range(N)]
    for i in range(N):
        already_combined = False
        col_vec = [tileset[j][i] for j in range(N)]
        col_vec.reverse()
        new_col_vec = []
        for j, k in enumerate(col_vec):
            if not new_col_vec and k != 0:
                new_col_vec.append(k)
            else:
                if k != 0 and new_col_vec[-1] == k and not already_combined:
                    new_col_vec[-1] += k
                    already_combined = True
                elif k != 0:
                    new_col_vec.append(k)
                    already_combined = False
        if len(new_col_vec) < N:
            new_col_vec += [0] * (N - len(new_col_vec))
        new_col_vec.reverse()
        for j in range(N):
            result[j][i] = new_col_vec[j]
    return result


def move_left(tileset: list[list[int]]) -> list[list[int]]:
    result = [[0 for _ in range(N)] for i in range(N)]
    for i in range(N):
        already_combined = False
        row_vec = [tileset[i][j] for j in range(N)]
        new_row_vec = []
        for j, k in enumerate(row_vec):
            if not new_row_vec and k != 0:
                new_row_vec.append(k)
            else:
                if k != 0 and new_row_vec[-1] == k and not already_combined:
                    new_row_vec[-1] += k
                    already_combined = True
                elif k != 0:
                    new_row_vec.append(k)
                    already_combined = False
        if len(new_row_vec) < N:
            new_row_vec += [0] * (N - len(new_row_vec))
        for j in range(N):
            result[i][j] = new_row_vec[j]
    return result


def move_right(tileset: list[list[int]]) -> list[list[int]]:
    result = [[0 for _ in range(N)] for i in range(N)]
    for i in range(N):
        already_combined = False
        row_vec = [tileset[i][j] for j in range(N)]
        row_vec.reverse()
        new_row_vec = []
        for j, k in enumerate(row_vec):
            if not new_row_vec and k != 0:
                new_row_vec.append(k)
            else:
                if k != 0 and new_row_vec[-1] == k and not already_combined:
                    new_row_vec[-1] += k
                    already_combined = True
                elif k != 0:
                    new_row_vec.append(k)
                    already_combined = False
        if len(new_row_vec) < N:
            new_row_vec += [0] * (N - len(new_row_vec))
        new_row_vec.reverse()
        for j in range(N):
            result[i][j] = new_row_vec[j]
    return result


def movement_list_maker(N:int, M:int) -> list[list[int]]:
    list_permut = []
    stack = []
    def dfs(init, M, stack):
        if M == 0:
            list_permut.append(stack[:])
            return
        else:
            #중복순열
            for i in range(1, N+1):
                stack.append(i)
                dfs(i, M-1, stack)
                stack.pop()
    dfs(1, M, stack)
    return list_permut
movement_list = movement_list_maker(4,5)

answer:int = 0
for movements in movement_list:
    tileset_copy = [[tileset[i][j] for j in range(N)] for i in range(N)]
    for k in movements:
        if k == 1:
            tileset_copy = move_up(tileset_copy)
        elif k == 2:
            tileset_copy = move_down(tileset_copy)
        elif k == 3:
            tileset_copy = move_left(tileset_copy)
        else:
            tileset_copy = move_right(tileset_copy)
    answer = max(answer, *[max(tileset_copy[l]) for l in range(N)])
print(answer)
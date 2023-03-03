# 1018 체스판 다시 칠하기

answer = 64
N, M = list(map(int, input().split(" ")))
chess_board: list[list[str]] = [list(input()) for r in range(N)]


def chess_board_checker(r_offset: int, c_offset: int) -> int:
    start_from_white = [32, 32]
    start_from_black = [32, 32]
    for x in range(8):
        for y in range(8):
            if chess_board[r_offset + y][c_offset + x] == "W":
                if (x + y) % 2:
                    start_from_black[1] -= 1
                else:
                    start_from_white[0] -= 1
            else:
                if (x + y) % 2:
                    start_from_white[1] -= 1
                else:
                    start_from_black[0] -= 1
    return min(sum(start_from_black), sum(start_from_white))


for r_offset in range(N - 7):
    for c_offset in range(M - 7):
        answer_sub = chess_board_checker(r_offset, c_offset)
        if answer_sub < answer:
            answer = answer_sub
print(answer)

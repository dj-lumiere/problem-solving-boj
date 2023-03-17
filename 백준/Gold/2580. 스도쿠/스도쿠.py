# 2580 스도쿠

sudoku_table: list[list[int]] = [list(map(int, input().split(" "))) for _ in range(9)]
sudoku_number_by_row: list[list[bool]] = [[True] + [False] * 9 for _ in range(9)]
sudoku_number_by_column: list[list[bool]] = [[True] + [False] * 9 for _ in range(9)]
sudoku_number_by_square: list[list[bool]] = [[True] + [False] * 9 for _ in range(9)]
sudoku_blank_number_deque: list[tuple[int, int]] = []
sudoku_filling_number_stack: list[int] = []

for col in range(9):
    for row in range(9):
        value = sudoku_table[row][col]
        if value == 0:
            sudoku_blank_number_deque.append((row, col))
        else:
            sudoku_number_by_column[col][value] = True
            sudoku_number_by_row[row][value] = True
            sudoku_number_by_square[((row // 3) * 3 + (col // 3))][value] = True
stack_length = len(sudoku_blank_number_deque)


def sudoku_solver(
    sudoku_table: list[list[int]],
    sudoku_number_by_row: list[list[bool]],
    sudoku_number_by_column: list[list[bool]],
    sudoku_number_by_square: list[list[bool]],
    stack_pointer: int,
):
    if stack_pointer == stack_length:
        return sudoku_table
    else:
        row, col = sudoku_blank_number_deque[stack_pointer]
        for i in range(1, 9 + 1):
            if (
                not sudoku_number_by_row[row][i]
                and not sudoku_number_by_column[col][i]
                and not sudoku_number_by_square[((row // 3) * 3 + (col // 3))][i]
            ):
                sudoku_table[row][col] = i
                sudoku_number_by_row[row][i] = True
                sudoku_number_by_column[col][i] = True
                sudoku_number_by_square[((row // 3) * 3 + (col // 3))][i] = True
                if sudoku_solver(
                    sudoku_table=sudoku_table,
                    sudoku_number_by_row=sudoku_number_by_row,
                    sudoku_number_by_column=sudoku_number_by_column,
                    sudoku_number_by_square=sudoku_number_by_square,
                    stack_pointer=stack_pointer + 1,
                ):
                    return sudoku_table
                sudoku_table[row][col] = 0
                sudoku_number_by_row[row][i] = False
                sudoku_number_by_column[col][i] = False
                sudoku_number_by_square[((row // 3) * 3 + (col // 3))][i] = False
        return None


if stack_length:
    sudoku_solver(
        sudoku_table=sudoku_table,
        sudoku_number_by_row=sudoku_number_by_row,
        sudoku_number_by_column=sudoku_number_by_column,
        sudoku_number_by_square=sudoku_number_by_square,
        stack_pointer=0,
    )

for i in range(9):
    print(*sudoku_table[i])
